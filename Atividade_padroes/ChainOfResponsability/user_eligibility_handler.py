from typing import Type
from User.user import User
from Composite.book import Book
from Repository.book_repository import BookRepository
from ChainOfResponsability.handler import Handler

class UserEligibilityHandler(Handler):
    def handle(self, request) -> None:
        user = request['user']
        if user.is_eligible():
            return super().handle(request)
        else:
            print(f"User {user.get_name()} has reached the loan limit.")
            return False