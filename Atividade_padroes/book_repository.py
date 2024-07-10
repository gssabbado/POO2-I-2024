from book import Book

class BookRepository:
    def __init__(self) -> None:
        self.__book_repository = []
    
    def add_book(self, id_book: str, title: str, author: str, category: str, publisher: str, year: str, available: bool) -> None:
        book = Book(id_book, title, author, category, publisher, year, available)
        self.__book_repository.append(book)
        print(f"Book registered!, ID: {book.get_book_id()}")

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
                print("Book found!")
            else:
                print("Book not found!")
            
    def get_book_repository(self)->list:
        return self.__book_repository
'''
#Testes
la = BookRepository()
la.add_book("id","titulo","autor","categoria","publicador","ano",True)
la.list_books()
la.find_book("id")
la.remove_book("id")
la.list_books()
la.remove_book("dkdk")
la.list_books()'''