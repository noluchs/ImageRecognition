# 2. Sprintabschluss

## Fazit vom Sprint 2?
Timeout-Einstellungen in AWS Lambda
AWS Lambda-Funktionen haben standardmäßig eine Timeout-Zeit von 3 Sekunden. Wenn Ihre Funktion länger läuft, erhalten Sie eine Timeout-Fehlermeldung. Sie können die Timeout-Zeit für Ihre Funktion in der AWS Management Console erhöhen.

Direktes Lesen von Dateien aus S3
Anstatt Dateien von S3 herunterzuladen und dann zu öffnen, können Sie die get_object Funktion von Boto3 verwenden, um Dateien direkt aus S3 zu lesen. Dies kann den Code vereinfachen und die Ausführungszeit reduzieren.

Verwendung von Boto3 für Gesichtserkennung
Die compare_faces Funktion von Boto3 kann verwendet werden, um die Ähnlichkeit zwischen zwei Gesichtern in verschiedenen Bildern zu vergleichen. Sie können die SimilarityThreshold Option verwenden, um den Grad der Ähnlichkeit festzulegen, der für eine Übereinstimmung erforderlich ist.

### Status Prozentual

| Dokumentation | Python | AWS Lamda | Website | Github Action |  
| - | :- | :-: | :-: | -: |  
| 10 % | 20 % | 10% | 0 % | 0% |

### Kanban Board

## Learnings für den Sprint 2



