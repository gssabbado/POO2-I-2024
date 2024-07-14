from typing import Type
from user import User
from book_repository import BookRepository

#Pronto, Ja testado
class TeacherUserType(User):
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
        self._score = 10
        self._max_book_limit = 10
    
    def get_user_id(self) -> str:
        return self._id_user

    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._score}")
    
    def is_eligible(self) -> bool:
        return self._score >= 0

    def can_borrow_more_books(self) -> bool:
        return len(self._book_history["id_book"]) < self._max_book_limit

    
    def reserve_book(self, repo:Type[BookRepository], id_book: str) -> None:
       book = repo.find_book(id_book)
       if book is not None and book.get_book_available():
            book.set_book_availability(False)
       else:
           print("Book not available.\n")


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
    
