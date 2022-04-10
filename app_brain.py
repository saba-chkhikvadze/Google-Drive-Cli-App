from drive_uploader import DriveUploader
from listeners.diplay_changed_listener import DisplayChangedListener
import os

class DriveAppBrain:

    def __init__(self) -> None:
        self.uploader_object = DriveUploader('./configs')

    def register_display_changed_listener(self, display_changed_listener : DisplayChangedListener):
        self.display_change_listener = display_changed_listener

    def create_drive_folder(self, folder_name) -> str:
        if not self.uploader_object.exists_folder_on_drive(folder_name=folder_name):
            self.uploader_object.create_folder_on_drive(folder_name=folder_name)
            self.display_change_listener.display_message(f'Succesfully created folder {folder_name}')
    
    def upload_file(self, file_name : str, parent_drive_folder : str, folder_path = '.') -> str:
        if not self.uploader_object.exists_folder_on_drive(parent_drive_folder):
            self.display_change_listener.display_message(f'folder {parent_drive_folder} doesn\'t exist on your drive')
        else:
            if self.uploader_object.upload_file(file_name=file_name, parent_folder_name=parent_drive_folder, file_path=folder_path):
                self.display_change_listener.display_message(f'Succesfully uploaded file {file_name} to {parent_drive_folder}')
        
    def get_folders_from_drive(self, num_folders = 1):
        files = self.uploader_object.list_files(num_folders)
        s = ''
        for file in files:
            self.display_change_listener.display_message(file)

    def invalid_command_handler(self):
        self.display_change_listener.display_message('invalid command')