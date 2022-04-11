from typing import Protocol

from listeners.input_listener import InputListener


class DisplayChangedListener(Protocol):
    
    def display_message(self, display : str):
        raise NotImplementedError

    def read_command(self):
        raise NotImplementedError
    
    def display_instructions(self):
        raise NotImplementedError

    def register_input_listener(self, input_listener : InputListener):
        raise NotImplementedError