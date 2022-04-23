from app_brain import DriveAppBrain
from ui import UI
import os

class DriveAppController:
    
    def __init__(self, view : UI, brain : DriveAppBrain) -> None:
        self.ui = view
        self.ui.register_input_listener(self)
        self.brain = brain
    

    def trigger_input(self, input : str):
        '''
        reads input, tokenizes it and acts accordingly
        '''

        tokens = input.strip().split(' ')
        try:
            command = tokens[0]
            if command == 'upload':
                filename = tokens[1]
                if len(tokens) == 2:
                    self.brain.upload_file(filename)
                    return
                parent_folder_name = tokens[2]
                if len(tokens) == 3:
                    self.brain.upload_file(filename, parent_folder_name)
                elif len(tokens) == 4:
                    folder_path = os.path.abspath(tokens[3])
                    self.brain.upload_file(filename, parent_folder_name, folder_path)
            elif command == 'list_files':
                if len(tokens[1:]) > 0:
                    num_files = int(tokens[1])
                    self.brain.get_folders_from_drive(num_files)
                else:
                    self.brain.get_folders_from_drive()
            elif command == 'create_folder':
                folder_name = tokens[1]
                self.brain.create_drive_folder(folder_name)
            elif command == 'download':
                file_name = ''
                for i in tokens[1:]:
                    file_name += f'{i} '
                file_name = file_name.strip()
                self.brain.download_file(file_name = file_name)
            elif command == 'help':
                self.brain.display_commands()
            elif command == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                self.brain.invalid_command_handler()
        except IndexError:
            self.brain.invalid_command_handler()
    def start(self):
        self.ui.read_command()
            
                    