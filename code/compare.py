import boto3
import botocore

def lambda_handler(event, context):
    s3_resource = boto3.resource('s3')
    s3_client = boto3.client('s3')
    rekognition = boto3.client('rekognition')

    bucket1 = s3_resource.Bucket('imagerekognition-s3-test')
    bucket2 = s3_resource.Bucket('imagerekognition-s3-test-2')

    for file1 in bucket1.objects.all():
        s3_client.download_file('imagerekognition-s3-test', file1.key, '/tmp/local-file1.jpg')
        for file2 in bucket2.objects.all():
            s3_client.download_file('imagerekognition-s3-test-2', file2.key, '/tmp/local-file2.jpg')
            
            with open('/tmp/local-file1.jpg', 'rb') as image1, open('/tmp/local-file2.jpg', 'rb') as image2:
                response = rekognition.compare_faces(
                    SourceImage={'Bytes': image1.read()},
                    TargetImage={'Bytes': image2.read()},
                    SimilarityThreshold=99
                )
                
                if response['FaceMatches']:
                    print(f"Die Bilder {file1.key} und {file2.key} stimmen zu mehr als 99% überein.")
                    