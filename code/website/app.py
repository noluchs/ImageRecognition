from flask import Flask, request, render_template
import boto3
import botocore
from werkzeug.utils import secure_filename

app = Flask(__name__)
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
rekognition = boto3.client('rekognition')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        s3_client.upload_file(filename, 'imagerekognition-s3-test', filename)
        
        bucket1 = s3_resource.Bucket('imagerekognition-s3-test')
        bucket2 = s3_resource.Bucket('imagerekognition-s3-test-2')
        matches = []
        
        for file1 in bucket1.objects.all():
            for file2 in bucket2.objects.all():
                if file1.key == filename:
                    s3_client.download_file('imagerekognition-s3-test', file1.key, '/tmp/local-file1.jpg')
                    s3_client.download_file('imagerekognition-s3-test-2', file2.key, '/tmp/local-file2.jpg')
                    
                    with open('/tmp/local-file1.jpg', 'rb') as image1, open('/tmp/local-file2.jpg', 'rb') as image2:
                        response = rekognition.compare_faces(
                            SourceImage={'Bytes': image1.read()},
                            TargetImage={'Bytes': image2.read()},
                            SimilarityThreshold=99
                        )
                        
                        if response['FaceMatches']:
                            matches.append(file2.key)
                            
        return render_template('results.html', matches=matches)
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)