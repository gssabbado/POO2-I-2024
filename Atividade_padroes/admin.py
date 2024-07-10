from typing import Type
from book_repository import BookRepository

class Admin:
    def __init__(self, name:str, id_admin:str, cpf:str) -> None:
        self.__name = name
        self.__id_admin = id_admin
        self.__cpf = cpf

    def add_book_to_repo(self, repo: Type[BookRepository], id_book: str, title: str, author: str, category: str, publisher: str, year: str, available: bool)->None:
        repo.add_book(id_book, title, author, category, publisher, year, available)
        
    def remove_book_from_repo(self, repo: Type[BookRepository], id_book: str)-> None:
        repo.remove_book(id_book)
    
    #Entender como o user_repository funciona, em especial o add user
    '''
    def find_user(self, repo:Type[UserRepository], id_user:str)->None:
        for user in repo.get_user_repository():
            if user.get_user_id() == id_user:
                print("User found!")
                print(user.get_user())
            else:
                print("User not found!")
    
    def add_user_to_repo(self, repo:Type[UserRepository], id_user:str) -> None:
        repo.add_user(user:Type[User]) #Ver isso aqui
        
    def remove_user(self, repo: Type[UserRepository], id_user:str) -> None:
        repo.remove_user(id_user)       

    def consult_history(self):
        pass

    def consult_score(self, repo: Type[UserRepository], id_user:str)-> int:
        for user in repo.get_user_repository():
            if user.get_user_id() == id_user:
                user.consult_score()
            else:
                print("User not found!")
    
    def uptade_score(self, repo: Type[UserRepository], id_user:str, score) -> None:
        for user in repo.get_user_repository():
            if user.get_user_id() == id_user:
                user.set_score(score)  
            else:
                print("User not found!")  '''  

    def reserve_book(self, repo: Type[BookRepository], id_book: str) -> None:
        for book in repo.get_book_repository():
            if book.get_book_id() == id_book:
                if book.get_book_available():
                    book.set_book_availalability(False)
                    print(f"Book {id_book} reserved.")
                else:
                    print(f"Book {id_book} is already reserved.")
                return
        print("Book not found!")
    



'''
#Exemplo

la = Admin("Nome", "ID", "CPF")
repo = BookRepository()
la.add_book_to_repo(repo, "AL", "AL", "AL", "AL", "AL", "AL", True)
la.reserve_book(repo, "AL") #Book AL reserved.
la.reserve_book(repo, "AL") #Book AL is already rereved.
la.reserve_book(repo, "A")  #Book not found!'''