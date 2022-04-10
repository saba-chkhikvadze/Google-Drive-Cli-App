from lib2to3.pgen2 import token
from soupsieve import match
from app_brain import DriveAppBrain
from drive_uploader import DriveUploader
from ui import UI


class DriveAppController:
    
    def __init__(self, view : UI, brain : DriveAppBrain) -> None:
        self.ui = view
        self.ui.register_input_listener(self)
        self.brain = brain
    

    def trigger_input(self, input : str):
        tokens = input.split(' ')
        try:
            command = tokens[0]
            if command == 'upload':
                print(tokens)
                filename = tokens[1]
                parent_folder_name = tokens[2]
                if len(tokens) == 3:
                    self.brain.upload_file(filename, parent_folder_name)
                    print(filename, parent_folder_name)
                elif len(tokens) == 4:
                    folder_path = tokens[3]
                    self.brain.upload_file(filename, parent_folder_name, folder_path)
            elif command == 'list_files':
                num_files = int(tokens[1])
                self.brain.get_folders_from_drive(num_files)
            elif command == 'create_folder':
                folder_name = tokens[1]
                self.brain.create_drive_folder(folder_name)
            else:
                self.brain.invalid_command_handler()
        except IndexError:
            self.brain.invalid_command_handler()
    def start(self):
        self.ui.read_command()
            
                    