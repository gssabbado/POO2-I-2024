from abc import ABC, abstractmethod
from typing import Type

#Tem que alterar o consult_history depois que tiver as funcinoaalidades em adm

class User(ABC):
    def __init__(self, name:str, id_user:str, cpf:str) -> None:
        self._name = name
        self._id_user = id_user
        self._cpf = cpf
        self._book_history = {}
        self.__score = 0

    @abstractmethod
    def consult_history(self) -> dict:
        pass

    @abstractmethod
    def consult_score(self) -> int:
        pass


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

    #def reserve_book(self, id_book: str) -> None:
    #   if id_book in list_of_books:   
    #       book.avalible = No       
    #   else:
    #       print("Book not found!")
    #
    #
   # def find_user(self, user: Type[User]) -> bool:
   #    for user in list_of_users:
   #        if user == list_of_users:
   #            print("User found!")
   #        else:
   #            print("User not found!")

#Testando:
student = StudentUserType("Joao", "ID","CPF")

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

teacher.consult_history()
teacher.consult_score()
teacher.pay_score()
