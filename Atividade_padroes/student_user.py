from user import User

# Pronto, ja foi testado
class StudentUserType(User):
    def __init__(self, name:str, id_user:str, cpf:str, email:str) -> None:
        super().__init__(name, id_user, cpf, email) 
        self._book_history = {
            "id_book": ["A"],
            "title": ["B"],
            "author": [],
            "category": [],
            "publisher": [],
            "year": [],   
        }
        self._score = 20
        self._max_book_limit = 0
    
    def get_user_id(self) -> str:
        return self._id_user

    def consult_history(self) -> dict:
        print(f"{self._name} history: {self._book_history}")
    
    def consult_score(self) -> int:
        print(f"{self._name} score: {self._score}")
    
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