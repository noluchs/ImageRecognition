from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import boto3
import os
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv("aws.env")

application = Flask(__name__)

s3 = boto3.client("s3",
    region_name=os.environ.get("REGION"),
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)

rekognition = boto3.client('rekognition',
    region_name=os.environ.get("REGION"),
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)


def resize_image(image, basewidth=300):  # Reduced from 500 to 300
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    return img


@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)

        # Resize the image before uploading to S3
        image = resize_image(file)
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)

        s3.upload_fileobj(image_io, os.environ.get("UPLOAD_BUCKET"), filename)
        matches = compare_faces(filename)
        if not matches:  # Check if matches list is empty
            return render_template('gallery.html', message="Kein Match gefunden")
        return render_template('gallery.html', matches=matches)
    return render_template('upload.html')

def compare_faces(uploaded_file_path):
    bucket = os.environ.get("COMPARE_BUCKET")
    matches = []
    for obj in s3.list_objects(Bucket=bucket)['Contents']:
        response = rekognition.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': os.environ.get("UPLOAD_BUCKET"),
                    'Name': uploaded_file_path
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': obj['Key']
                }
            },
            SimilarityThreshold=99
        )
        if response['FaceMatches']:
            matches.append(obj['Key'])
    return matches

if __name__ == '__main__':
    application.run(debug=True)