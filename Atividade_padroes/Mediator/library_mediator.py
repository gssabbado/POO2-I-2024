from typing import Type
from User.user import User
from User.student_user import StudentUserType
from User.admin_user import AdminUserType
from User.teacher_user import TeacherUserType
from Composite.book import Book
from Repository.book_repository import BookRepository
from ChainOfResponsability.handler import Handler
from ChainOfResponsability.handler_chain import BookAvailabilityHandler, UserEligibilityHandler, LoanLimitHandler

class LibraryMediator:
    def __init__(self, book_repository: Type[BookRepository]) -> None:
        self._book_repository = book_repository
        
        # Inicializando a cadeia de responsabilidade
        self._chain = BookAvailabilityHandler(book_repository)
        self._chain.set_next(UserEligibilityHandler()).set_next(LoanLimitHandler())
        
    def borrow_book(self, user: Type[User], id_book: str) -> None:
        request = {'user': user, 'id_book': id_book}
        if self._chain.handle(request):
            book = self._book_repository.find_book(id_book)
            if book:
                book.set_book_availability(False)
                user._book_history["id_book"].append(book.get_book_id())
                user._book_history["title"].append(book.get_book()["title"])
                user._book_history["author"].append(book.get_book()["author"])
                user._book_history["category"].append(book.get_book()["category"])
                user._book_history["publisher"].append(book.get_book()["publisher"])
                user._book_history["year"].append(book.get_book()["year"])
                print(f"Book {id_book} borrowed by {user._name}.")
            else:
                print(f"Book {id_book} not found.")
        else:
            print(f"Book {id_book} cannot be borrowed by {user._name}.")
            
    def return_book(self, user: Type[User], id_book: str) -> None:
        book = self._book_repository.find_book(id_book)
        if book:
            book.set_book_availability(True)
            if id_book in user._book_history["id_book"]:
                idx = user._book_history["id_book"].index(id_book)
                del user._book_history["id_book"][idx]
                del user._book_history["title"][idx]
                del user._book_history["author"][idx]
                del user._book_history["category"][idx]
                del user._book_history["publisher"][idx]
                del user._book_history["year"][idx]
                print(f"Book {id_book} returned by {user._name}.")
            else:
                print(f"Book {id_book} was not borrowed by {user._name}.")
        else:
            print(f"Book {id_book} not found.")
    
    def consult_book(self, id_book: str) -> None:
        book = self._book_repository.find_book(id_book)
        if book:
            print(f"Book {id_book} found:")
            print(book.get_book())
        else:
            print(f"Book {id_book} not found.")
    
    def consult_user_history(self, user: Type[User]) -> None:
        history = user.consult_history()
        print(f"User {user._name}'s book history: {history}")
    
    def consult_user_score(self, user: Type[User]) -> None:
        score = user.consult_score()
        print(f"User {user._name}'s score: {score}")
        
    def reserve_book(self, user: Type[User], id_book: str) -> None:
        if isinstance(user, TeacherUserType):
            user.reserve_book(self._book_repository, id_book)
        else:
            print("Only teachers can reserve books.")
