## Projektabschluss / Fazit

### Rückblick auf das Projekt

Das Projekt begann mit dem klaren Ziel, eine Webanwendung zur Bilderkennung zu entwickeln, die auf Amazon Rekognition basiert. Die Umsetzung erfolgte in drei Sprints, wobei jeder Sprint spezifische Ziele und Aufgaben hatte. Der erste Sprint konzentrierte sich auf den Aufbau der Projektstruktur und die Implementierung der grundlegenden Bilderkennungsfunktion mit AWS Rekognition. Der zweite Sprint fokussierte sich auf die Fertigstellung des Python-Skripts zur Bildervergleichsfunktion, während der dritte Sprint die Herausforderungen der Webseitenerstellung und Deployment mit sich brachte.

### Was lief gut

Die Implementierung der Bilderkennungsfunktion mit Amazon Rekognition war erfolgreich und lieferte gute Ergebnisse. Trotz einiger Herausforderungen wurden die Ziele der ersten beiden Sprints erreicht, wenn auch nicht ohne Anpassungen und Überlegungen. Die Sprint-Reviews waren konstruktiv, und die identifizierten Learnings trugen zur kontinuierlichen Verbesserung bei. Die Einrichtung von GitHub Actions zur Automatisierung von Tests, Builds und Deployments erleichterte den Entwicklungsprozess.

### Probleme bei dem Projekt

Der enge Zeitplan führte dazu, dass nicht alle ursprünglich geplanten Ziele erreicht werden konnten. Dies war insbesondere bei der Webseitenentwicklung im letzten Sprint spürbar. Die Entscheidung, von Lambda zu Flask und schließlich zu AWS Elastic Beanstalk zu wechseln, brachte unerwartete Schwierigkeiten mit sich. Die Standard-Timeout-Einstellungen von AWS Lambda führten zu Herausforderungen bei der Ausführung des Python-Skripts im zweiten Sprint.

### Learnings fürs nächste Projekt (bezüglich Projektplanung)

Eine frühzeitige Auseinandersetzung mit Tools wie AWS Elastic Beanstalk und GitHub Actions kann zu einer reibungsloseren Integration führen. Eine realistischere Zeitplanung ist entscheidend, um besser auf unvorhergesehene Probleme reagieren zu können. Ein tieferes Verständnis der verwendeten Tools wie Flask, AWS Elastic Beanstalk und Boto3 ist unerlässlich, um technische Herausforderungen effizienter zu meistern. Eine direkte Dokumentation während des Entwicklungsprozesses spart Zeit und erleichtert das Debugging.

### Nächste Schritte für das Projekt

1. **Backend-Aufbau für Gallery Events:** Implementierung von Funktionen zur Erstellung, Bearbeitung und Löschung von Gallery Events.

2. **Sicherheit und Authentifizierung:** Implementierung von Sicherheitsmaßnahmen und Authentifizierung für den Zugriff auf Gallery Events.

3. **Elastizitätsprüfung mit AWS Elastic Beanstalk:** Durchführung von Tests unter erhöhtem Benutzerandrang, um die Skalierbarkeit der Anwendung zu gewährleisten.

### Fazit

Trotz der Herausforderungen war das Projekt insgesamt erfolgreich. Die Learnings aus den Sprints bieten wertvolle Einsichten für zukünftige Projekte, und die identifizierten Bereiche zur Verbesserung werden die Effizienz und den Erfolg kommender Projekte fördern. Der Abschluss des Projekts markiert nicht nur einen Meilenstein in der technologischen Entwicklung, sondern auch in der Fähigkeit zur Planung und Umsetzung komplexer Aufgaben.


