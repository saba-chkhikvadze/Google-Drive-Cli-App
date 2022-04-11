from drive_uploader import DriveUploader
from listeners.diplay_changed_listener import DisplayChangedListener
import os

class DriveAppBrain:

    def __init__(self) -> None:
        self.uploader_object = DriveUploader('./configs')



    def register_display_changed_listener(self, display_changed_listener : DisplayChangedListener):
        '''
        Registers new displaychangelistener object to listend to changes of content to display and notify view about it
        '''
        self.display_change_listener = display_changed_listener

    def create_drive_folder(self, folder_name):
        '''
        Create new folder on google drive of current user

        @param folder_name: name of folder to create on drive
        '''
        if not self.uploader_object.exists_folder_on_drive(folder_name=folder_name):
            self.uploader_object.create_folder_on_drive(folder_name=folder_name)
            self.display_change_listener.display_message(f'Succesfully created folder {folder_name}')
    
    def upload_file(self, file_name : str, parent_drive_folder : str, folder_path = '.'):
        '''
        Upload file with file_name to users google drive

        @param file_name: name of local file to upload
        @param parent_drive_folder: name of folder to upload in (google drive folder)
        @param folder_path: absolute path to folder to upload ("." by default)
        '''
        if not self.uploader_object.exists_folder_on_drive(parent_drive_folder):
            self.display_change_listener.display_message(f'folder {parent_drive_folder} doesn\'t exist on your drive')
        else:
            if self.uploader_object.upload_file(file_name=file_name, parent_folder_name=parent_drive_folder, file_path=folder_path):
                self.display_change_listener.display_message(f'Succesfully uploaded file {file_name} to {parent_drive_folder}')
        
    def get_folders_from_drive(self, num_folders = 1):
        '''
        lists N files/folders from user's google drive

        @param num_folders: max number of files/folders to display
        '''
        files = self.uploader_object.list_files(num_folders)
        s = ''
        for file in files:
            self.display_change_listener.display_message(file)
        
    def display_commands(self):
        '''
        display default commands for use
        '''
        self.display_change_listener.display_instructions()

    def invalid_command_handler(self):
        self.display_change_listener.display_message('invalid command')