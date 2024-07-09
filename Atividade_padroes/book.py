class Book (object):
    def __init__(self, id_book: str, title: str, author: str, category: str, publisher: str, year: str, available: bool) -> None:
        self._id_book = id_book
        self._title = title
        self._author = author
        self._category = category
        self._publisher = publisher
        self._year = year
        self._available = available
    
    def set_book(self, id_book: str = None, title: str = None, author: str = None, category: str = None, publisher: str = None, year: str = None, available: bool = None):
        if id_book is not None:
            self._id_book = id_book
        if title is not None:
            self._title = title
        if author is not None:
            self._author = author
        if category is not None:
            self._category = category
        if publisher is not None:
            self._publisher = publisher
        if year is not None:
            self._year = year
        if available is not None:
            self._available = available
               
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
    

#### Teste ####

book3 = Book('666', 'Me ajuda Deus', 'Lucifer Cristo', 'Horror', 'Inferno Astral', '1994', True)

print(book3.get_book())

book3.set_book(title="Me ajuda Satanas", category="Gospel") 

print(book3.get_book())  