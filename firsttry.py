import boto3

def lambda_handler(event, context):
    s3_bucket_name = 'your-s3-bucket-name'
    image_name = 'your-image-name'
    gallery_bucket_name = 'your-gallery-bucket-name'

    client = boto3.client('rekognition')

    response = client.detect_faces(
        Image={
            'S3Object': {
                'Bucket': s3_bucket_name,
                'Name': image_name,
            }
        },
        Attributes=['ALL']
    )

    if 'FaceDetails' in response:
        face_ids = [face['FaceId'] for face in response['FaceDetails']]

        for face_id in face_ids:
            compare_response = client.compare_faces(
                SourceImage={
                    'S3Object': {
                        'Bucket': s3_bucket_name,
                        'Name': image_name,
                    }
                },
                TargetImage={
                    'S3Object': {
                        'Bucket': gallery_bucket_name,
                        'Name': face_id,
                    }
                },
            )

            if 'FaceMatches' in compare_response:
                for match in compare_response['FaceMatches']:
                    print(f"Found matching face: {match['Face']['FaceId']}")

    return {
        'statusCode': 200,
        'body': 'Face detection completed'
    }
