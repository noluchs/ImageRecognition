import boto3

BUCKET = "imagerekognition-s3-test"
KEY_SOURCE = "noah-2.jpg"
KEY_TARGET = "noah-3.jpg"

def lambda_handler(event, context):
    source_face, matches = compare_faces(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)

    # Print über das zu vergelichende Bild ob ein Gesich gefunden
    if source_face:
        print("Source Face ({Confidence}%)".format(**source_face))
    else:
        print("No source face found in the image.")

    # Print falls die Gesichter in beiden Bilder übereinstimmen
    for match in matches:
        face = match.get('Face', {})
        similarity = match.get('Similarity', 0)
        print("Target Face ({Confidence}%)".format(**face))
        print("  Übereinstimmung der Gesichter : {}%".format(similarity))

def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.compare_faces(
        SourceImage={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        TargetImage={
            "S3Object": {
                "Bucket": bucket_target,
                "Name": key_target,
            }
        },
        SimilarityThreshold=threshold,
    )

    source_face = response.get('SourceImageFace', {})
    matches = response.get('FaceMatches', [])

    return source_face, matches
