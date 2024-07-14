#Interface para os outros handlers
from abc import ABC, abstractmethod
from typing import Type, Optional

class Handler(ABC):
    def __init__(self) -> None:
        self._next_handler: Optional[Type['Handler']] = None
    
    def set_next(self, handler: Type['Handler']) -> Type['Handler']:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request) -> None:
        if self._next_handler:
            return self._next_handler.handle(request)       
        return True