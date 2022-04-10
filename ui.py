from abc import ABC, abstractmethod
from typing import Protocol
from listeners.diplay_changed_listener import DisplayChangedListener

from listeners.input_listener import InputListener


class UI(ABC):

    @abstractmethod
    def read_command(self):
        raise NotImplementedError

    @abstractmethod    
    def display_message(self, message : str):
        raise NotImplementedError
    
    @abstractmethod
    def register_input_listener(self, input_listener : InputListener):
        raise NotImplementedError

    