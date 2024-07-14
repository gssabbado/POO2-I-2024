from abc import ABC, abstractmethod
from typing import Type
from Repository.book_repository import BookRepository

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

    @abstractmethod
    def is_eligible(self) -> bool:
        pass

    @abstractmethod
    def can_borrow_more_books(self) -> bool:
        pass

    @abstractmethod
    def update(self) -> None:
        pass