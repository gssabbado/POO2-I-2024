from abc import ABC, abstractmethod
from typing import Type
from book_repository import BookRepository

#Tem que alterar o consult_history depois que tiver as funcinoaalidades em adm
class User:
    def __init__(self, name:str, id_user:str, cpf:str, email:str) -> None:
        self._name = name
        self._id_user = id_user
        self._cpf = cpf
        self._email = email
        
    @abstractmethod
    def consult_history(self) -> dict:
        pass

    @abstractmethod
    def consult_score(self) -> int:
        pass

    @abstractmethod
    def get_user_id(self) -> str:
        pass

'''    
    def set_score(self, score: int) -> None:
        self._score += score

    def get_user_id(self) -> str:
        print("teste")
        return self._id_user
'''

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