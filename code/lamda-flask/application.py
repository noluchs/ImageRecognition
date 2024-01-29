from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import boto3
import os
from dotenv import load_dotenv

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

@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, os.environ.get("UPLOAD_BUCKET"), filename)
        matches = compare_faces(filename)
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