from typing import Protocol


class InputListener(Protocol):
    def trigger_input(self, input): 
        raise NotImplementedError