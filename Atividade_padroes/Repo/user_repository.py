from ..user import User


class RepositoryUser:
    def __init__(self) -> None:
        self.__user_repository = []
        
    def add_user(self, user: User) -> None:
        self.__user_repository.append(user)
        print(f"User {user.get_user_info()['name']} added successfully.")
        
    def find_user_id(self):
        