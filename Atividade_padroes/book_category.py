from book import Book
from library_component import LibraryComponent
from typing import List, Optional, Union

class BookCategory(LibraryComponent):
    def __init__(self, id_category: str, name: str, parent_category: Optional['BookCategory'] = None) -> None:
        self._id_category = id_category
        self._name = name
        self._parent_category = parent_category
        self._children: List[LibraryComponent] = []
        
    def add(self, component):
        self._children.append(component)
        
    def remove(self, component):
        self._children.remove(component)
    
    def get_children(self):
        return self._children
    
    def get_category(self):
        return self._name
    
    def get_parent_children(self):
        return self._parent_category
  
    def display(self, indent = 0):
        print(' ' * indent + f"{self._name} (ID: {self._id_category})")
        for child in self._children:
            child.display(indent + 2)    

    