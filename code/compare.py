import boto3

def lambda_handler(event, context):
    # S3-Bucket und Dateiname des Eingangsbildes
    input_bucket = 'dein-input-bucket'
    input_image = 'dein-input-bild.jpg'
    
    # S3-Bucket für die Galerie
    gallery_bucket = 'dein-gallery-bucket'
    
    # Amazon Rekognition Client erstellen
    rekognition = boto3.client('rekognition')
    
    # Gesichtserkennung auf dem Eingangsbild durchführen
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': input_bucket,
                'Name': input_image
            }
        },
        Attributes=['DEFAULT']
    )
    
    # Liste der erkannten Gesichter
    faces = response['FaceDetails']
    
    # Gesichter in der Galerie vergleichen und ähnliche Gesichter anzeigen
    for face in faces:
        face_id = face['FaceId']
        
        # Vergleich der Gesichter in der Galerie
        response = rekognition.search_faces_by_image(
            CollectionId='deine-galerie',
            Image={
                'S3Object': {
                    'Bucket': gallery_bucket,
                    'Name': input_image
                }
            },
            FaceMatchThreshold=80,
            MaxFaces=10
        )
        
        # Ähnliche Gesichter anzeigen
        for match in response['FaceMatches']:
            similar_face = match['Face']
            similarity = match['Similarity']
            
            print(f"Ähnliches Gesicht gefunden: FaceId={similar_face['FaceId']}, Ähnlichkeit={similarity}%")
