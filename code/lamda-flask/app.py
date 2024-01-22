# Importieren der benötigten Module
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import boto3
from dotenv import load_dotenv

# Laden der Umgebungsvariablen aus der Datei 's3-acceskey.env'
load_dotenv("s3-acceskey.env")

# Initialisieren der Flask-Anwendung
app = Flask(__name__)

# Erstellen eines boto3-Clients für AWS S3
s3 = boto3.client("s3",
    aws_access_key_id=os.environ.get("S3_KEY"),  # AWS-Zugangsschlüssel aus den Umgebungsvariablen holen
    aws_secret_access_key=os.environ.get("S3_SECRET"),  # AWS-Geheimschlüssel aus den Umgebungsvariablen holen
)

# Definieren der Route für die Anwendung
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # Wenn die Anfragemethode POST ist
    if request.method == 'POST':
        # Datei aus der Anfrage holen
        file = request.files['file']
        # Sichern des Dateinamens
        filename = secure_filename(file.filename)
        # Hochladen der Datei auf S3
        s3.upload_fileobj(file, 'imagerekognition-s3-upload', filename)
        # Rückgabe einer Erfolgsmeldung
        return 'Datei erfolgreich hochgeladen'
    # Wenn die Anfragemethode nicht POST ist, wird die Vorlage 'index.html' gerendert
    return render_template('index.html')

# Ausführen der Anwendung
if __name__ == '__main__':
    app.run(debug=True)


