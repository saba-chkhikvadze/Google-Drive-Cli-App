from listeners.input_listener import InputListener
from ui import UI


class Cli(UI):
    
    def read_command(self):
        self.display_instructions()
        while True:
            command = input('>>> ')
            if command == 'exit':
                print('>>> bye...')
                break
            self.input_listener.trigger_input(command)
    
    def display_instructions(self):
        print('>>> upload <filename> <folder name on drive> <abs path to file>')
        print('>>> list files <number of files>')
        print('>>> create_folder <folder name>')

    def display_message(self, message : str) -> None:
        print(f'>>> {message}')

    def register_input_listener(self, input_listener : InputListener):
        self.input_listener = input_listener