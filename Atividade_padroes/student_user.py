from user import User

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
        self._score = 0
        self._max_book_limit = 0
    
    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._score}")
    
    
    # Adicionar esse método no outro arquivo "ADMIN"
    def add_books(self, id_book, title, author, category, publisher, year) -> dict:
        self._book_history["id_book"].append(id_book)
        self._book_history["title"].append(title)
        self._book_history["author"].append(author)
        self._book_history["category"].append(category)
        self._book_history["publisher"].append(publisher)
        self._book_history["year"].append(year)
        return self._book_history