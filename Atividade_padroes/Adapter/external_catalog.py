from abc import ABC, abstractmethod
from typing import List, Optional, Union

class ExternalCatalog(ABC):
    @abstractmethod
    def add_external_book(self, external_book) -> None:
        pass
    
    @abstractmethod
    def remove_external_book(self, external_book_id: str) -> None:
        pass
    
    @abstractmethod
    def list_external_book(self) -> List[dict]:
        pass
    
    @abstractmethod
    def find_external_book(self, external_book_id: str) -> Optional[dict]:
        pass