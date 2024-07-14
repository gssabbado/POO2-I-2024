from typing import List, Optional, Union
from Adapter.external_catalog import ExternalCatalog
from Repository.book_repository import BookRepository
from Composite.book import Book

class ExternalCatalogAdapter(ExternalCatalog):
        def __init__(self, book_repository: BookRepository) -> None:
                self._book_repository = book_repository
                
        def add_external_book(self, external_book) -> None:
            book = Book(
                id_book = external_book["id_book"],
                title = external_book["title"],
                author = external_book["author"],
                category = external_book["category"],
                publisher = external_book["publisher"],
                year = external_book["year"],
                available = external_book["available"]
            )
            self._book_repository.add_book(book)
            
        def remove_external_book(self, external_book_id: str) -> None:
            self._book_repository.remove_book(external_book_id)
         
        def list_external_book(self) -> List[dict]:
            books = self._book_repository.get_book_repository()
            return [book.get_book() for book in books]
        
        def find_external_book(self, external_book_id: str) -> Optional[dict]:
            book = self._book_repository.find_book(external_book_id)
            if book is not None:
                return book.get_book()
            return None           