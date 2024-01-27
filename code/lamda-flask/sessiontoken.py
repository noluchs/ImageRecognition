import boto3

# Erstellen Sie einen STS-Client
sts = boto3.client('sts')

# Rufen Sie Sitzungs-Token ab
response = sts.get_session_token()

# Drucken Sie die temporären Anmeldedaten aus
print('AccessKeyId:', response['Credentials']['AccessKeyId'])
print('SecretAccessKey:', response['Credentials']['SecretAccessKey'])
print('SessionToken:', response['Credentials']['SessionToken'])