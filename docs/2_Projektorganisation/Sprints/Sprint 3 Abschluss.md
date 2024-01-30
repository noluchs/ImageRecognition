#   Sprint 3 Abschluss

Der dritte und letzte Sprint des Projekts brachte einige große Herausforderungen mit sich, vor allem in Bezug auf das Rendering der Website und die Darstellung der Ergebnisse der Lambda-Funktion. Ursprünglich war geplant, Lambda zu verwenden, aber die Realität zwang mich, meine Strategie zu überdenken und mich für Flask zu entscheiden, ein Python-Framework für das Rendering von Webseiten. Diese Entscheidung brachte unerwartete Schwierigkeiten mit sich.

Die Webseite konnte nicht erfolgreich aus dem Template-Verzeichnis gerendert werden und die eingeschränkten Debugging-Möglichkeiten von Flask führten zu einem hohen Zeitaufwand bei der Fehlersuche. Das Hosting wurde schließlich über Elastic Beanstalk realisiert, was jedoch aufgrund von Berechtigungsproblemen und Schwierigkeiten beim Upload der Applikation mit den spezifischen Anforderungen von Elastic Beanstalk verbunden war. Diese Herausforderungen konnten kurz vor der Fertigstellung gemeistert werden.

Zusätzlich war das Design einer ansprechenden Webseite für den Dienst eine weitere Anforderung. Die Einrichtung des Deployments erfolgte über AWS Pipeline auf einem separaten Git, da aus Zeitgründen auf eine detaillierte Auseinandersetzung mit Github Actions verzichtet wurde.

### Status Prozentual

|Dokumentation|Python|AWS Lambda|Website|Github Action|
|---|---|---|---|---|
|100 %|100 %|100%|100 %|100 %|

### Kanban Board
![](attachments/Pasted%20image%2020240130222812.png)


## Learnings für die nächste Arbeit

Ein tieferes Verständnis der verwendeten Tools wie Flask, AWS Elastic Beanstalk und Boto3 ist unerlässlich, um technische Herausforderungen effizienter zu meistern. Es wurde deutlich, wie wichtig eine direkte Dokumentation während des Entwicklungsprozesses ist, um Zeit zu sparen und das Debugging zu erleichtern. Eine bessere Planung und realistischere Zeitvorgaben sind notwendig, um besser auf unvorhergesehene Probleme reagieren zu können. Ein tieferes Verständnis der Berechtigungen und Upload-Anforderungen von AWS Elastic Beanstalk ist entscheidend für einen reibungslosen Betrieb. Eine frühzeitige Auseinandersetzung mit Tools wie Github Actions kann zu einer reibungsloseren Integration und weniger Zeitdruck führen.

Diese Learnings haben nicht nur zur technologischen Weiterentwicklung beigetragen, sondern unterstreichen auch die Wichtigkeit einer durchdachten Planung und kontinuierlichen Auseinandersetzung mit neuen Technologien. Sie dienen als Grundlage für die kontinuierliche Verbesserung zukünftiger Projekte. Eine ausführlichere Zusammenfassung des Projekts findent man Hier [Projektabschluss und Fazit](../Projektabschluss%20und%20Fazit.md) 