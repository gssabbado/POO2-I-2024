from User.user import User
from book_availability_notifier import BookAvailabilityNotifier
from typing import Type


#Se der tempo, arrumar o inglês
class UserRepository:
    def __init__(self, notifier: Type[BookAvailabilityNotifier]) -> None:
        self.__user_repository = []
        self.__notifier = notifier
        
    def add_user(self, user: User) -> None:
        self.__user_repository.append(user)
        self.__notifier.register(user)
        print(f"User {user.get_user_id()} added successfully.")
        
    def find_user_id(self, id_user: str):
        for user in self.__user_repository:
            if user.get_user_id() == id_user:
                print("User found!")
            else:
                print("User not found!")
    
    def list_users(self) -> None:
        for user in self.__user_repository:
            print(user.get_user())
    
    def remove_user(self, id_user:str) -> None:
        removed = False
        for user in self.__user_repository:
            if user.get_user_id() == id_user:
                self.__user_repository.remove(user)
                self.__notifier.unregister(user)
                print(f"User {user.get_user_id()} removed.")
                removed = True
                break
        if not removed:
                print("User not registered!")

    def get_user_repository(self) -> list:
        return self.__user_repository