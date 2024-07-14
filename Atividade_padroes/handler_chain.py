#dividir esse arquivo
from typing import Type
from user import User
from book import Book
from book_repository import BookRepository
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
    
class UserEligibilityHandler(Handler):
    def handle(self, request) -> None:
        user = request['user']
        if user.is_eligible():
            return super().handle(request)
        else:
            print(f"User {user.get_name()} has reached the loan limit.")
            return False
        
class LoanLimitHandler(Handler):
    def handle(self, request) -> None:
        user = request['user']
        if user.can_borrow_more_books():
            return super().handle(request)            
        else:
            print(f"User {user.get_name()} has reached the loan limit.")
            return False