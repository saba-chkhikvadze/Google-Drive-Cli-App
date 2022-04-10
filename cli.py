
from listeners.input_listener import InputListener
from ui import UI


class Cli(UI):
    
    def read_command(self):
        while True:
            command = input('>>> ')
            if command == 'exit':
                break
            self.input_listener.trigger_input(command)
    
    def display_instructions(self):
        pass

    def display_message(self, message : str) -> None:
        print(f'>>> {message}')

    def register_input_listener(self, input_listener : InputListener):
        self.input_listener = input_listener