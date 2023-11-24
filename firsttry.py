import boto3
from PIL import Image, ImageFilter

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    rekognition_client = boto3.client('rekognition')

    # Definieren Sie Ihren eigenen Bucket-Namen und Dateinamen
    bucket = 'imagerekognition-s3'
    source_image = 'DSC_0125.jpg'
    target_image = 'DSC_0129.jpg'

    # Vergleichen Sie das Quellbild mit dem Zielbild
    response = rekognition_client.compare_faces(
        SourceImage={'S3Object': {'Bucket': bucket, 'Name': source_image}},
        TargetImage={'S3Object': {'Bucket': bucket, 'Name': target_image}}
    )

    # Überprüfen Sie, ob die Gesichter identisch sind
    for face_match in response['FaceMatches']:
        if face_match['Similarity'] > 90:  # Ändern Sie den Schwellenwert nach Bedarf
            # Laden Sie das Zielbild herunter
            s3_client.download_file(bucket, target_image, '/tmp/target.jpg')
            
            # Machen Sie das Bild unscharf
            img = Image.open('/tmp/target.jpg')
            blurred_img = img.filter(ImageFilter.BLUR)
            
            # Speichern Sie das unscharfe Bild
            blurred_img.save('/tmp/blurred_target.jpg')
            
            # Laden Sie das unscharfe Bild in den S3-Bucket hoch
            s3_client.upload_file('/tmp/blurred_target.jpg', bucket, 'blurred_target.jpg')

    return {
        'statusCode': 200,
        'body': 'Bildverarbeitung abgeschlossen'
    }
