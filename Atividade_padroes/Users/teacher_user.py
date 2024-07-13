from typing import Type
from user import User
from book_repository import BookRepository

#Pronto, Ja testado
class TeacherUserType(User):
    def __init__(self, name:str, id_user:str, cpf:str, email:str) -> None:
        super().__init__(name, id_user, cpf, email)
        self._book_history = {}
        self._score = 0
        self._max_book_limit = 0
    
    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._score}")
    
    def reserve_book(self, repo:Type[BookRepository], id_book: str) -> None:
       book = repo.find_book(id_book)
       if book is not None and book.get_book_available():
            book.set_book_availalability(False)
       else:
           print("Book not available.\n")