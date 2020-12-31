from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

project_name = "Demo-Project-Chatbot-abhi"
project_id = "chatbot-2613"

credentials = GoogleCredentials.get_application_default()
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
project_body = {
    'name': project_name,
    'projectId': project_id
}
request = service.projects().create(body=project_body)
request.execute()
print("-------------------------------------")
print("Project created successfully")
print("-------------------------------------")