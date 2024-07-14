from User.user import User
from typing import Type
from Repository.book_repository import BookRepository

# Pronto, ja foi testado
class StudentUserType(User):
    def __init__(self, name:str, id_user:str, cpf:str, email:str) -> None:
        super().__init__(name, id_user, cpf, email) 
        self._book_history = {
            "id_book": [],
            "title": [],
            "author": [],
            "category": [],
            "publisher": [],
            "year": [],   
        }
        self._score = 20
        self._max_book_limit = 5
    
    def get_user_id(self) -> str:
        return self._id_user

    def is_eligible(self) -> bool:
        return self._score > 0

    def can_borrow_more_books(self) -> bool:
        return len(self._book_history["id_book"]) < self._max_book_limit

    def update( self, id_book: str) -> None:
        print(f"Hey {self._name}, the book {id_book} is now available")

    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._score}")
    
    def get_user(self):
        return {
                "id_user": self._id_user,
                "name": self._name,
                "cpf": self._cpf,
                "email": self._email,
                "book_hitory": self._book_history,
                "score": self._score,
                "max_book_limit": self._max_book_limit
                }
    
    def borrow_book(self, repo: Type[BookRepository], id_book: str) -> None:
        if not self.is_eligible():
            print(f"{self._name} isn't eligible to borrow books.")
            return
        if not self.can_borrow_more_books():
            print(f"{self._name} has reached the maximum book limit.")
            return
        book = repo.find_book(id_book)
        if book and book.get_book_available():
            book.set_book_availability(False)
            self._book_history["id_book"].append(book.get_book_id())
            self._book_history["title"].append(book.get_book_title())
            self._book_history["author"].append(book.get_book_author())
            self._book_history["category"].append(book.get_book_category())
            self._book_history["publisher"].append(book.get_book_publisher())
            self._book_history["year"].append(book.get_book_year())
            print(f"Book {id_book} borrowed by {self._name}.")
        else:
            print("Book not available.")

    def return_book(self, repo: Type[BookRepository], id_book: str) -> None:
        if id_book in self._book_history["id_book"]:
            book = repo.find_book(id_book)
            if book:
                book.set_book_availability(True)
            print(f"Book {id_book} returned by {self._name}.")
            self.update(id_book)
        else:
            print(f"Book {id_book} not found in {self._name}'s history.") 