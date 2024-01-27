import io
import logging
import time
from flask import Flask, render_template, request, Response, stream_with_context
from werkzeug.utils import secure_filename
import boto3
import botocore
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
from PIL import Image

# Set up logging
#logging.basicConfig(level=logging.DEBUG)  # Change this to logging.INFO to disable debug logging

load_dotenv("s3-acceskey.env")

def file_exists_in_s3(bucket_name, file_name):
    s3 = boto3.client("s3",
        region_name="us-east-1",
        aws_access_key_id=os.environ.get("S3_KEY"),
        aws_secret_access_key=os.environ.get("S3_SECRET"),
    )
    try:
        s3.head_object(Bucket=bucket_name, Key=file_name)
        return True
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            raise

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

        # Return the path of the uploaded file on S3
        uploaded_file_path = f"{filename}"
        #uploaded_file_path = f"imagerekognition-s3-upload/{filename}"

        # Call compare_faces function
        matches = compare_faces(uploaded_file_path)

        return render_template('gallery.html', matches=matches)

    return render_template('upload.html')


def compare_faces(uploaded_file_path):
    bucket = s3_resource.Bucket('imagerekognition-s3-compare')
    matches = []

    try:
        # Retry up to 5 times with a delay of 2 seconds between each attempt
        for _ in range(5):
            try:
                if not file_exists_in_s3('imagerekognition-s3-upload', uploaded_file_path):
                    time.sleep(2)  # Wait for 2 seconds before the next attempt
                else:
                    break
            except ClientError as e:
                if e.response['Error']['Code'] == 'NoSuchKey':
                    time.sleep(2)  # Wait for 2 seconds before the next attempt
                else:
                    raise
        else:
            logging.error(f"The uploaded file {uploaded_file_path} does not exist.")
            return matches


        for obj in bucket.objects.all():
            try:
                # Check if the target image exists before trying to get it
                if not file_exists_in_s3('imagerekognition-s3-compare', obj.key):
                    logging.error(f"The object {obj.key} does not exist.")
                    continue

                response = rekognition.compare_faces(
                    SourceImage={
                        'S3Object': {
                            'Bucket': 'imagerekognition-s3-upload',
                            'Name': uploaded_file_path
                        }
                    },
                    TargetImage={
                        'S3Object': {
                            'Bucket': 'imagerekognition-s3-compare',
                            'Name': obj.key
                        }
                    },
                    SimilarityThreshold=99
                )

                if response['FaceMatches']:
                    matches.append(obj.key)
                    logging.debug(f'Match found: {obj.key}')

            except botocore.exceptions.BotoCoreError as e:
                logging.error(f"BotoCoreError occurred: {str(e)}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {str(e)}")

    except botocore.exceptions.BotoCoreError as e:
        logging.error(f"BotoCoreError occurred: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

    return matches



if __name__ == '__main__':
    application.run(debug=True)