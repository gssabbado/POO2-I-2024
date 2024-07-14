from User.user import User
from typing import Type

class BookAvailabilityNotifier:
    def __init__(self) -> None:
        self._observers = []

    def register(self, user: User) -> None:
        self._observers.append(user)

    def unregister(self, user: User) -> None:
        self._observers.remove(user)

    def notify_users(self, book_id: str) -> None:
        for observer in self._observers:
            observer.update(book_id)