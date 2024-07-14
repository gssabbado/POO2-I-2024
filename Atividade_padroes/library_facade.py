from typing import Type
from User.user import User
from User.student_user import StudentUserType
from User.admin_user import AdminUserType
from User.teacher_user import TeacherUserType
from Repository.book_repository import BookRepository
from library_mediator import LibraryMediator

class LibraryFacade:
    def __init__(self, book_repository: Type[BookRepository]) -> None:
        self._mediator = LibraryMediator(book_repository)
    
    def borrow_book(self, user: Type[User], id_book: str) -> None:
        print(f"Request to borrow book {id_book} by {user._name}")
        self._mediator.borrow_book(user, id_book)
    
    def return_book(self, user: Type[User], id_book: str) -> None:
        print(f"Request to return book {id_book} by {user._name}")
        self._mediator.return_book(user, id_book)
    
    def consult_book(self, id_book: str) -> None:
        print(f"Request to consult book {id_book}")
        self._mediator.consult_book(id_book)
    
    def consult_user_history(self, user: Type[User]) -> None:
        print(f"Request to consult history of user {user._name}")
        self._mediator.consult_user_history(user)
    
    def consult_user_score(self, user: Type[User]) -> None:
        print(f"Request to consult score of user {user._name}")
        self._mediator.consult_user_score(user)
    
    def reserve_book(self, user: Type[User], id_book: str) -> None:
        print(f"Request to reserve book {id_book} by {user._name}")
        self._mediator.reserve_book(user, id_book)
