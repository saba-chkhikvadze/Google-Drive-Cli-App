from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import os
import time

class DriveUploader:
    def __init__(self, configs_dir : str) -> None:
        scopes = ['https://www.googleapis.com/auth/drive']
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        self.configs_dir = configs_dir
        if os.path.exists(f'{self.configs_dir}/token.json'):
            creds = Credentials.from_authorized_user_file(f'{self.configs_dir}/token.json', scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f'{self.configs_dir}/credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'{self.configs_dir}/token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('drive', 'v3', credentials=creds)
        except HttpError as error:
            print(f'An error occurred: {error}')

    def list_files(self, size : int):
        results = self.service.files().list(
            pageSize = size, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            return []
        else:
            return [f'file : {item["name"]}' for item in items]

    def exists_folder_on_drive(self, folder_name : str) -> bool:
        response = self.service.files().list(q = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'", spaces = 'drive').execute()
        if not response['files']:
            return False
        return True

    def create_folder_on_drive(self, folder_name : str) -> bool:
        if not self.exists_folder_on_drive(folder_name=folder_name):
            file_metadata = {
                "name" : folder_name,
                "mimeType" : "application/vnd.google-apps.folder"
            }
            file = self.service.files().create(body = file_metadata, fields = "id").execute()
            return True
        return False

    def get_folder_id(self, folder_name : str):
        if self.exists_folder_on_drive(folder_name=folder_name):
            response = self.service.files().list(q = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'", spaces = 'drive').execute()
            return response['files'][0]['id']
        print('file doesn\'t exist on drive')
        return None

    def upload_file(self, file_name : str, parent_folder_name : str, file_path = '.', ) -> bool:
        if not self.exists_folder_on_drive(parent_folder_name):
            return False
        parent_folder_id = self.get_folder_id(parent_folder_name)
        files = os.listdir(file_path)
        if file_name in files:
            file_metadata = {
                'name' : file_name,
                'parents' : [parent_folder_id]
            }
            media = MediaFileUpload(f'{file_path}/{file_name}')
            try:
                file_upload = self.service.files().create(body = file_metadata,
                                                      media_body = media,
                                                      fields = 'id'      
                                                    ).execute()
            except HttpError:
                return False
        return True 
