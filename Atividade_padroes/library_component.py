from abc import ABC, abstractmethod
from typing import List, Optional, Union

class LibraryComponent(ABC):
    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass
    
    @abstractmethod
    def add(self, component: "LibraryComponent") -> None:
        pass
    
    @abstractmethod
    def remove(self, component: "LibraryComponent") -> None:
        pass
    
    @abstractmethod
    def get_children(self) -> List["LibraryComponent"]:
        pass
    