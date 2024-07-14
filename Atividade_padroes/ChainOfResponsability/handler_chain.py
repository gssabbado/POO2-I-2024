#dividir esse arquivo
from typing import Type
from User.user import User
from book import Book
from Repository.book_repository import BookRepository
from handler import Handler

class BookAvailabilityHandler(Handler):
    def __init__(self, book_repository: Type[BookRepository]) -> None:
        super().__init__()
        self._book_repository = book_repository
            
    def handle(self, request) -> None:
        id_book = request.get("id_book")
        book = self._book_repository.find_book(request['id_book'])
        if book and book.get_book_available():
            return super().handle(request)
        else:
            print(f"Book {id_book} is not available.")
            return False
    