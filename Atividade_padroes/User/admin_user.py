from typing import Type
from User.user import User
from Composite.book import Book
from Repository.book_repository import BookRepository
from Repository.user_repository import UserRepository

# Pronto, ja foi testado
class AdminUserType(User):
    def __init__(self, name:str, id_user:str, cpf:str, email:str) -> None:
        super().__init__(name, id_user, cpf, email) 
    
    def get_user_id(self) -> str:
        return self._id_user
    
    def search_user(self, repo:Type[UserRepository], id_user:str)->None:
        user_found = False
        for user in repo.get_user_repository():
            if user.get_user_id() == id_user:
                print("User found!")
                user_found = True
                return user
        if not user_found:
            print("User not found!")

    def find_user(self, repo:Type[UserRepository], id_user:str)->None:
        user = self.search_user(repo, id_user)
        user.get_user()

    def consult_history_of_user(self, repo: Type[UserRepository], id_user:str)-> int:
        user = self.search_user(repo, id_user)
        user.consult_history()

    def consult_score_of_user(self, repo: Type[UserRepository], id_user:str)-> int:
        user = self.search_user(repo, id_user)
        user.consult_score()

    def uptade_score(self, repo: Type[UserRepository], id_user:str, score: int) -> None:
        user = self.search_user(repo, id_user)
        user._score += score
        return user.consult_score()
    
    def add_book_to_repo(self, repo: Type[BookRepository], book:Type[Book])->None:
        repo.add_book(book)
            
    def add_user_to_repo(self, repo:Type[UserRepository], user: Type[User]) -> None:
        repo.add_user(user)
        
    def remove_book_from_repo(self, repo: Type[BookRepository], id_book: str)-> None:
        repo.remove_book(id_book)

    def get_user(self):
        return {
                "id_user": self._id_user,
                "name": self._name,
                "cpf": self._cpf,
                "email": self._email,
                }
    def reserve_book(self, repo:Type[BookRepository], id_book: str) -> None:
       book = repo.find_book(id_book)
       if book is not None and book.get_book_available():
            book.set_book_availability(False)
            print(f"Book {id_book} reserved.")
       else:
           print("Book not available.\n")

    def remove_user_from_repo(self, repo: Type[UserRepository], id_user:str) -> None:
        repo.remove_user(id_user)   
    
    # Aqui o Admin pode pegar quantos livros quiser e está sempre elegivel para pegar os livros    
    def is_eligible(self) -> bool:
        return False

    def can_borrow_more_books(self) -> bool:
        return False 