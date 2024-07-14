from book import Book
from typing import Type

class BookRepository:
    def __init__(self) -> None:
        self.__book_repository = []

    #Retirar/Diminuir as mensagens
    def add_book(self, book:Type[Book]) -> None:
        self.__book_repository.append(book)
        print(f"Book registered!, ID: {self.__book_repository[-1].get_book_id()}")

    def remove_book(self, id_book:str) -> None:
        removed = False
        for book in self.__book_repository:
            if book.get_book_id() == id_book:
                self.__book_repository.remove(book)
                print(f"Book {book.get_book_id()} removed.")
                removed = True
                break
        if not removed:
            print("Book not registered!")
    
    def list_books(self) -> None:
        for book in self.__book_repository:
            print(book.get_book())
    
    def find_book(self, id_book:str) -> None:
        for book in self.__book_repository:
            if book.get_book_id() == id_book:
                print("Book found! A\n")
                return book
        print("Book not found! B")
        return None
            
    #Ver a necessidade disso        
    def get_book_repository(self)->list:
        return self.__book_repository
    
    def teste(self):
        self.add_book("id","titulo","autor","categoria","publicador","ano",True)

