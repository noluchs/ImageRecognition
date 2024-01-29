# Entwicklung einer Bilderkennungs-Webanwendung mit Amazon Rekognition, Python, AWS Lambda und GitHub Actions


Dieses Projekt zielt darauf ab, eine Webanwendung zu entwickeln, die eine Bilderkennungsfunktion als REST-API bereitstellt. Die Anwendung wird in der Lage sein, Bilder zuzuordnen. Das bedeutet, man kann ein Bild von sich hochladen und das eigene Gesicht wird mit allen Bildern verglichen. Alle Bilder, auf denen man sichtbar ist, werden angezeigt. Die Bilderkennungsfunktion wird mit Amazon Rekognition implementiert und auf AWS gehostet. GitHub Actions wird verwendet, um den Code automatisch zu testen, zu bauen und auf AWS Lambda hochzuladen, wenn Änderungen am Quellcode vorgenommen werden.



## Inhaltsverzeichnis
### Aufbau Umgebung Lamda
[AWS Rekognition Ersterversuch](docs/Aufbau%20Umgebung/Lamda%20Function/AWS%20Rekognition%20Ersterversuch.md)
[AWS  Rekognition Gallery](docs/Aufbau%20Umgebung/Lamda%20Function/AWS%20%20Rekognition%20Gallery.md)

### [Flask](docs/Aufbau%20Umgebung/Flask/readme.md)
[Upload S3 Bucket](docs/Aufbau%20Umgebung/Flask/Upload%20S3%20Bucket.md)
[Flask Applikation](docs/Aufbau%20Umgebung/Flask/Flask%20Apllikation.md)

### AWS Beanstalk
[AWS Beanstalk einrichten](docs/Aufbau%20Umgebung/AWS%20Beanstalk/AWS%20Beanstalk%20einrichten.md)
[Github Actions](docs/Aufbau%20Umgebung/AWS%20Beanstalk/Github%20Actions.md)



### Projektmanagement
#### Sprint 
[Sprint 1 Abschluss](docs/Projektorganisation/Sprints/Sprint%201%20Abschluss.md)
[Sprint 2 Abschluss](docs/Projektorganisation/Sprints/Sprint%202%20Abschluss.md)
[Sprint 3 Abschluss](docs/Projektorganisation/Sprints/Sprint%203%20Abschluss.md)

## Literaturverzeichnis
[Quellen](Anhang/Quellen.md)
[Recherche](Anhang/Recherche.md)
[Sachmittel](Anhang/Sachmittel.md)
## Einleitung
### Problemstellung

In der heutigen Welt spielt die Bilderkennung eine entscheidende Rolle in verschiedenen Anwendungsfeldern, darunter soziale Medien, Sicherheit, Gesichtserkennung und persönliche Identifikation. Die Erstellung einer Bilderkennungsanwendung, die auf einfache Weise die Identifikation von Personen in Bildern ermöglicht, ist von großem Interesse. Dieses Projekt zielt darauf ab, eine solche Anwendung zu entwickeln, die auf einer REST-API basiert und mithilfe von Amazon Rekognition, einem leistungsstarken Cloud-basierten Bilderkennungsdienst, arbeitet. Die Anwendung ermöglicht es Benutzern, ein Bild von sich hochzuladen und die automatische Identifikation von Bildern, auf denen sie sichtbar sind, durchzuführen.

### Ziele

Die Hauptziele dieses Projekts sind:

·       Identifikation von Personen in Bildern: Das Hauptziel des Projekts besteht darin, eine benutzerfreundliche Webanwendung zu erstellen, die es Benutzern ermöglicht, ein Bild von sich hochzuladen und automatisch alle Bilder zu identifizieren, auf denen sie sichtbar sind. Dies umfasst die Verwendung von Amazon Rekognition, um Gesichter in den hochgeladenen Bildern zu erkennen und mit einer Datenbank von Bildern zu vergleichen.

·       Implementierung einer zuverlässigen REST-API: Ein weiteres Ziel des Projekts ist die Entwicklung einer robusten und skalierbaren REST-API, die die Bilderkennungsfunktion bereitstellt. Diese API sollte benutzerfreundlich sein und es den Benutzern ermöglichen, Bilder hochzuladen und die Ergebnisse der Bilderkennung abzurufen.

·       Automatisierung und Continuous Integration: Das Projekt zielt darauf ab, GitHub Actions für die Automatisierung von Tests, Builds und Bereitstellung auf AWS Lambda zu nutzen. Dies bedeutet, dass Änderungen am Quellcode automatisch getestet und bei Erfolg auf die AWS-Plattform hochgeladen werden. Dieses Ziel fördert die Entwicklungseffizienz und die Bereitstellung von zuverlässigem Code.

Diese Ziele zielen darauf ab, eine nützliche und effiziente Bilderkennungsanwendung zu entwickeln, die auf Amazon Rekognition basiert und Benutzern die Möglichkeit bietet, Bilder von sich selbst hochzuladen und automatisch alle relevanten Bilder zu finden, auf denen sie sichtbar sind. Gleichzeitig wird die Entwicklung und Bereitstellung der Anwendung durch Automatisierung optimiert.  

### Terminplan

Der grobe Terminplan für dieses Projekt ist in drei Sprints unterteilt:

·       **Sprint 1: Entwicklung der Bilderkennungsfunktion**. Dies beinhaltet das . Alle Schritte werden dokumentiert.

·       **Sprint 2: Entwicklung der Webanwendung und Integration der Bilderkennungsfunktion**. Die Webanwendung wird so gestaltet, dass sie benutzerfreundlich ist und eine einfache Möglichkeit bietet, Bilder hochzuladen und die Ergebnisse anzuzeigen. Alle Schritte werden dokumentiert.

·       **Sprint 3: Einrichtung von GitHub Actions zur Automatisierung des Test-, Build- und Deployment-Prozesses.** Dies beinhaltet das Schreiben von Tests für den Code, das Einrichten des Build-Prozesses in GitHub Actions und das Konfigurieren des Deployments auf AWS Lambda. Abschließende Dokumentation des gesamten Projekts wird erstellt und eine Präsentation zur Vorstellung des Projekts wird vorbereitet.



### Vorgaben, Methoden und Werkzeuge

Die im Projekt eingesetzten Methoden und Werkzeuge sind Python, Amazon Rekognition für die Bilderkennungsfunktion, AWS S3 Bucket für das Speichern der Bilder, AWS Lambda für das Hosting der Anwendung und GitHub Actions für die Automatisierung des Test-, Build- und Deployment-Prozesses.

### Risiken

Die Hauptrisiken in diesem Projekt sind:

·       Technische Schwierigkeiten: Es kann technische Herausforderungen geben, insbesondere bei der Implementierung der Bilderkennungsfunktion und der Integration in die Webanwendung. Dies kann durch gründliche Planung und Tests gemindert werden.

·       Zeitmanagement: Das Projekt hat einen straffen Zeitplan, daher könnte es schwierig sein, alle Aufgaben rechtzeitig abzuschließen. Dies kann durch effektives Zeitmanagement und Priorisierung von Aufgaben gemindert werden.








Diese Dokumentation ist in Obsidian geschrieben für die beste Qualität, die Arbeit mit Obsidian öffnen [Obsidian Herunterladen](https://obsidian.md/)