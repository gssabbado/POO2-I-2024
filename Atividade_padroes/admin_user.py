from typing import Type
from user import User
from book import Book
from book_repository import BookRepository
from user_repository import RepositoryUser

#Adaptar para ser um tipo de User, tirar o init e aplicar os métodos de consult_histpry e consult_score
class AdminUserType(User):
    def __init__(self, name:str, id_user:str, cpf:str, email:str) -> None:
        super().__init__(name, id_user, cpf, email) 
    
    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._User__score}")

    def add_book_to_repo(self, repo: Type[BookRepository], id_book: str, title: str, author: str, category: str, publisher: str, year: str, available: bool)->None:
        repo.add_book(id_book, title, author, category, publisher, year, available)
    
    def add_book_to_repo(self, repo: Type[BookRepository], book: Type[Book])->None:
        repo.add_book(book)
        
    def add_user_to_repo(self, repo:Type[RepositoryUser], user: Type[User]) -> None:
        repo.add_user(user) #Ver isso aqui
    
    def add_user_to_repo(self, repo:Type[RepositoryUser], id:str, nome:str, cpf_in:str) -> None:
        user = User(id_user=id, name=nome, cpf=cpf_in)
        repo.add_user(user) #Ver isso aqui
        
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