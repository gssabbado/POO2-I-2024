from abc import ABC, abstractmethod
from typing import Type
from book_repository import BookRepository

#Tem que alterar o consult_history depois que tiver as funcinoaalidades em adm

class User(ABC):
    def __init__(self, name:str, id_user:str, cpf:str) -> None:
        self._name = name
        self._id_user = id_user
        self.__cpf = cpf
        self._book_history = {}
        self.__score = 0

    @abstractmethod
    def consult_history(self) -> dict:
        pass

    @abstractmethod
    def consult_score(self) -> int:
        pass
    
    def set_score(self, score: int) -> None:
        self.__score += score

    def get_user(self):
        return {
            "name": self._name,
            "User ID": self._id_user,
            "CPF": self.__cpf,
            "Book History": self._book_history,
            "Score": self.__score
        }
    
    def get_user_id(self) -> str:
        return self._id_user

class StudentUserType(User):
    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._User__score}")
    
    def pay_score(self) -> None:
        if self._User__score == 0:
            print("No debt to pay")
        else:
            self._User__score = 0
            print("Debt payed")  

class TeacherUserType(User):
    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._User__score}")
    
    def pay_score(self) -> None:
        if self._User__score == 0:
            print("No debt to pay")
        else:
            self._User__score = 0
            print("Debt payed")

    def reserve_book(self, repo:Type[BookRepository], id_book: str) -> None:
       book = repo.find_book(id_book)
       if book is not None and book.get_book_available():
            book.set_book_availalability(False)
       else:
           print("Book not available.")
    
    
   # def find_user(self, user: Type[User]) -> bool:
   #    for user in list_of_users:
   #        if user == list_of_users:
   #            print("User found!")
   #        else:
   #            print("User not found!")

'''
#Testando:
student = StudentUserType("Joao", "ID","CPF")
repo = BookRepository()
repo.teste()
print(len(repo.get_book_repository()))
repo.find_book("id")
student.consult_score()
student.pay_score()
student.consult_history()
student._book_history["Livro A"] = {"author": "Autor A", "year": 2023}
student.consult_history()
student._User__score = 100 #Só colocando uma dívida
student.consult_score()
student.pay_score()
student.consult_score()

teacher = TeacherUserType("Prof","IdProf","CpfProf")

teacher.reserve_book(repo, id_book="id")
teacher.reserve_book(repo, id_book="id")

teacher.consult_history()
teacher.consult_score()
teacher.pay_score()
'''