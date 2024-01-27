import io
import logging
from flask import Flask, render_template, request, Response, stream_with_context
from werkzeug.utils import secure_filename
import boto3
import botocore
import os
import tempfile
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Change this to logging.INFO to disable debug logging

load_dotenv("s3-acceskey.env")

application = Flask(__name__)

s3 = boto3.client("s3",
    region_name="us-east-1",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)

s3_resource = boto3.resource('s3')

rekognition = boto3.client('rekognition',
    region_name="us-east-1",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)


@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)

        # Read the file into memory
        file_bytes = file.read()

        # Create a file-like object from the bytes for uploading to S3
        file_obj = io.BytesIO(file_bytes)
        s3.upload_fileobj(file_obj, 'imagerekognition-s3-upload', filename)
        logging.debug('File uploaded successfully')

        # Call compare_faces function
        matches = compare_faces(file_bytes)

        return render_template('gallery.html', matches=matches)

    return render_template('upload.html')


def compare_faces(file_bytes):
    bucket = s3_resource.Bucket('imagerekognition-s3-compare')
    matches = []

    for obj in bucket.objects.all():
        try:
            tmp = tempfile.NamedTemporaryFile(delete=False)
            bucket.download_file(obj.key, tmp.name)
            with open(tmp.name, 'rb') as image:
                response = rekognition.compare_faces(
                    SourceImage={'Bytes': file_bytes},
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

    return matches



if __name__ == '__main__':
    application.run(debug=True)