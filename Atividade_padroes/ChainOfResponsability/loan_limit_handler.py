from typing import Type
from User.user import User
from book import Book
from Repository.book_repository import BookRepository
from handler import Handler

class LoanLimitHandler(Handler):
    def handle(self, request) -> None:
        user = request['user']
        if user.can_borrow_more_books():
            return super().handle(request)            
        else:
            print(f"User {user.get_name()} has reached the loan limit.")
            return False