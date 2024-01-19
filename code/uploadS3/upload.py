import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import boto3
from dotenv import load_dotenv

load_dotenv("s3-acceskey.env")  # Name Ihrer Umgebungsvariablendatei


app = Flask(__name__)
s3 = boto3.client("s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, 'imagerekognition-s3-upload', filename)
        return 'File uploaded successfully'
    return render_template('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)