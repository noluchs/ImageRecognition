# AWS  Rekognition Ersterversuch

In diesem ersten Versuch wird die Interaktion zwischen Amazon Rekognition, Lambda und dem S3 Bucket getestet. Ein Python-Skript wird in Lambda ausgeführt, das zwei Bilder vergleicht und die Übereinstimmung der darauf abgebildeten Gesichter bewertet.
![](../attachments/Pasted%20image%2020231124230529.png)

## Aufbau
### Erstellung einer IAM-Rolle für Lambda

Zunächst erstellen wir eine IAM-Rolle, die Zugriffsrechte auf den S3-Service und AmazonRekognitionFullAccess hat. Diese Rolle wird später für den Lambda-Service benötigt und der Lambda-Funktion zugewiesen.
![](../attachments/Pasted%20image%2020231124161910.png)
### Erstellung einer Lambda-Funktion in Python

Hier erstellen wir die Lambda-Funktion mit dem Namen “imagerekognition-lambda” und weisen ihr die zuvor erstellte Berechtigungsrolle zu.


![](../attachments/Pasted%20image%2020231124162207.png)


### Erstellung eines S3-Speichers

Wir erstellen einen Amazon S3-Bucket namens “imagerekognition-s3-test”, in dem die Bilder gespeichert werden. Dabei stellen wir sicher, dass sich der Bucket in derselben AWS-Region wie die Lambda-Funktion befindet.

![](../attachments/Pasted%20image%2020231124162422.png)

## Erster Test

Das Python-Skript verwendet die Funktion `compare_faces`, um zwei angegebene Bilder zu vergleichen. Es analysiert die Gesichter auf den Bildern und gibt die Übereinstimmungsrate als Prozentsatz aus. Die Funktion `compare_faces` nutzt den AWS-Dienst Rekognition zur Gesichtserkennung. Die Ergebnisse werden dann ausgegeben, wobei die Ähnlichkeit der erkannten Gesichter in Prozent angegeben wird.

```
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


```

### Resultat

Das Ergebnis des Tests zeigt, dass Amazon Rekognition zu 99% sicher ist, dass auf den Bildern dieselbe Person abgebildet ist. Dies zeigt die hohe Genauigkeit und Zuverlässigkeit von Amazon Rekognition bei der Gesichtserkennung.

```
START RequestId: 115e1242-bc90-4d76-aed8-0c1c956b10b3 Version: $LATEST
Source Face (99.99951171875%)
Target Face (99.99942779541016%)
Übereinstimmung der Gesichter : 99.98184204101562%
END RequestId: 115e1242-bc90-4d76-aed8-0c1c956b10b3
REPORT RequestId: 115e1242-bc90-4d76-aed8-0c1c956b10b3	Duration: 1948.24 ms	Billed Duration: 1949 ms	Memory Size: 128 MB	Max Memory Used: 75 MB	Init Duration: 265.47 ms
```


![](../attachments/Pasted%20image%2020231127144521.png)