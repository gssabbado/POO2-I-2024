#Book é Leaf
from library_component import LibraryComponent
from typing import List

class Book (LibraryComponent):
    #Mudar para privado
    def __init__(self, id_book: str, title: str, author: str, category: str, publisher: str, year: str, available: bool) -> None:
        self._id_book = id_book
        self._title = title
        self._author = author
        self._category = category
        self._publisher = publisher
        self._year = year
        self._available = available
    
    def set_book_availability(self, available: bool) -> None:
        self._available = available
        

    def get_book_available(self) -> bool:
            return self._available

    def get_book(self):
        return {
                "id_book": self._id_book,
                "title": self._title,
                "author": self._author,
                "category": self._category,
                "publisher": self._publisher,
                "year": self._year,
                "available": self._available
                }
    
    def get_book_id(self) -> str:
        return self._id_book
    
    def display(self, indent: int = 0) -> None:
        print(' ' * indent + f"Book: {self._title} by {self._author} (ID: {self._id_book})")
 
    def add(self, component: "LibraryComponent") -> None:
        raise NotImplementedError("Cannot add to a leaf component.\n")
        
    def remove(self, component: "LibraryComponent") -> None:
        raise NotImplementedError("Cannot remove from a leaf componet.\n")
 
    def get_children(self) -> List["LibraryComponent"]:
        return []