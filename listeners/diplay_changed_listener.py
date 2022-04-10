from typing import Protocol


class DisplayChangedListener(Protocol):
    
    def display_message(self, display : str):
        raise NotImplementedError