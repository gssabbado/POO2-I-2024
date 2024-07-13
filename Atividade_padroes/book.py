#Book é Leaf

class Book (object):
    #Mudar para privado
    def __init__(self, id_book: str, title: str, author: str, category: str, publisher: str, year: str, available: bool) -> None:
        self._id_book = id_book
        self._title = title
        self._author = author
        self._category = category
        self._publisher = publisher
        self._year = year
        self._available = available
    
    def set_book_availalability(self, available: bool) -> None:
        self._available = available
        print("DEU")

    def get_book_available(self) -> bool:
            return self._available

    def get_book(self):
        return {
                "id_book": self._id_book,
                "title": self._title,
                "author": self._author,
                "category": self._category,
                "publisher": self._publisher,
                "year": self._year,
                "available": self._available
                }
    
    def get_book_id(self) -> str:
        return self._id_book
    
'''
#### Teste ####

book3 = Book('666', 'Me ajuda Deus', 'Lucifer Cristo', 'Horror', 'Inferno Astral', '1994', True)

print(book3.get_book())

book3.set_book(title="Me ajuda Satanas", category="Gospel") 

print(book3.get_book())  '''