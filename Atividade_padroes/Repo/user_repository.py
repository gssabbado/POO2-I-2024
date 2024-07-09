from ..user import User


class RepositoryUser:
    def __init__(self) -> None:
        self.__user_repository = []
        
    def add_user(self, user: User) -> None:
        self.__user_repository.append(user)
        print(f"User {user.get_user_info()['name']} added successfully.")
        
    def find_user_id(self, id_user: str):
        for user in self.__user_repository:
            if user.get_user_id() == id_user:
                print("User found!")
            else:
                print("User not found!")
    
    def user_list(self) -> None:
        for user in self.__user_repository:
            print(user.get_user())
    
    def remove_user(self, id_user:str) -> None:
        removed = False
        for user in self.__user_repository:
            if user.get_user_id() == id_user:
                self.__user_repository.remove(user)
                print(f"User {user.get_book_id()} removed.")
                removed = True
                break
            if not removed:
                print("User not registered!")
         
