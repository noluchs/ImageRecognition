# Bilder in S3 Bucket hochladen

Um den ersten Schritt in  Flask zu machen habe ich den ersten Teil der Applikation umgesetzt und zwar das Upload der Bilder zu dem AWS S3. 


## Service User
Wir erstellen einen Service User der dazu Berechtigt ist die Bilder in die AWS S3 Storage zu laden.  Dies wir dann über einen Access Key erledigt der dann im Code aneghängt wird.
### Berechtigung

![](attachments/Pasted%20image%2020240117154044.png)

### Acces Key
![](attachments/Pasted%20image%2020240117154421.png)


## Code

## Flask S3 Upload Anwendung

Dieses Skript ist eine einfache Flask-Anwendung, die es Benutzern ermöglicht, Dateien in einen AWS S3-Bucket hochzuladen. 
### Benötigte Module
```python
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import boto3
from dotenv import load_dotenv
```

### Umgebungsvariablen

Die AWS-Zugangsschlüssel und der Geheimschlüssel werden aus Umgebungsvariablen geladen, die in der Datei `s3-acceskey.env` gesetzt sind.

```python
load_dotenv("s3-acceskey.env")
```

### Flask-Anwendung

Eine Flask-Anwendung wird initialisiert und ein boto3-Client für AWS S3 wird erstellt.

```python
app = Flask(__name__)
s3 = boto3.client("s3",
    aws_access_key_id=os.environ.get("S3_KEY"),  
    aws_secret_access_key=os.environ.get("S3_SECRET"),  
)
```

### Route

Die Funktion `upload_file` behandelt sowohl GET- als auch POST-Anfragen an die Root-URL (`/`). 

```python
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, 'imagerekognition-s3-upload', filename)
        return 'Datei erfolgreich hochgeladen'
    return render_template('index.html')
```

Wenn die Anfragemethode POST ist, holt sie die Datei aus der Anfrage, sichert den Dateinamen und lädt die Datei in den S3-Bucket hoch. Wenn der Upload erfolgreich ist, gibt sie eine Erfolgsmeldung zurück. Wenn die Anfragemethode nicht POST ist, rendert sie die Vorlage `index.html`.

### Anwendung ausführen

```python
if __name__ == '__main__':
    app.run(debug=True)
```

Die Anwendung wird ausgeführt, wenn das Skript direkt aufgerufen wird.

## Website

Die Website ist einfach aufgebaut man kann ein Bild hochladen sobald dies erfolgreich ist zeigt es von dem Flask die Nachricht an das der Upload erfolgreich war
```
<!DOCTYPE html>  
<html>  
<body>  
  
<h2>Upload File</h2>  
<form action="/" method="post" enctype="multipart/form-data">  
  Select image to upload:  
  <input type="file" name="file" id="file">  
  <input type="submit" value="Upload Image" name="submit">  
</form>  
  
</body>  
</html>
```



# Test


![](attachments/Pasted%20image%2020240122204847.png)


![](attachments/Pasted%20image%2020240122204909.png)

![](attachments/Pasted%20image%2020240122204945.png)