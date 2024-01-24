import logging
from flask import Flask, render_template, request, Response, stream_with_context
from werkzeug.utils import secure_filename
import boto3
import botocore
import os
from dotenv import load_dotenv
import tempfile

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Change this to logging.INFO to disable debug logging

load_dotenv("s3-acceskey.env")

application = Flask(__name__)

s3 = boto3.client("s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)

s3_resource = boto3.resource('s3')
rekognition = boto3.client('rekognition')

def generate(file):
    with file.stream as f:
        data = f.read(1024)
        while len(data) > 0:
            yield data
            data = f.read(1024)

@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file.stream, 'imagerekognition-s3-upload', filename)
        logging.debug('File uploaded successfully')
        return 'File uploaded successfully'
    return render_template('upload.html')

@application.route('/compare', methods=['POST'])
def compare_faces():
    file = request.files['file']
    filename = secure_filename(file.filename)
    s3.upload_fileobj(file.stream, 'imagerekognition-s3-upload', filename)

    bucket = s3_resource.Bucket('imagerekognition-s3-compare')
    matches = []

    for obj in bucket.objects.all():
        try:
            tmp = tempfile.NamedTemporaryFile(delete=False)

            bucket.download_file(obj.key, tmp.name)
            with open(tmp.name, 'rb') as image:
                response = rekognition.compare_faces(
                    SourceImage={'Bytes': file.stream.read()},
                    TargetImage={'Bytes': image.read()},
                    SimilarityThreshold=99
                )

                if response['FaceMatches']:
                    matches.append(obj.key)
                    logging.debug(f'Match found: {obj.key}')

        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                logging.error("The object does not exist.")
            else:
                raise

    return render_template('gallery.html', matches=matches)

if __name__ == '__main__':
    application.run(debug=True)