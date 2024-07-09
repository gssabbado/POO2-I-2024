from book import Book

class BookCategory:
    def __init__(self, id_category: str, name: str, parent_category: 'BookCategory' = None) -> None:
        self._id_category = id_category
        self._name = name
        self._parent_category = parent_category
        self._children = []
        
    def add(self, component):
        self._children.append(component)
        
    def remove(self, component):
        self._children.remove(component)
    
    def get_children(self):
        return self._children
    
    def get_category(self):
        return self._name
    
    def get_parent_children(self):
        return self._parent_category
    
    def add_sub_category(self, sub_category: 'BookCategory'):
        self._children.append(sub_category)
        
    def get_sub_category(self):
        return [child for child in self._children if isinstance(child, BookCategory)]
    
    def display(self, indent=0):
        print(' ' * indent + f"{self._name} (ID: {self._id_category})")
        for child in self._children:
            if isinstance(child, Book):
                book_info = child.get_book()
                print(' ' * (indent + 2) + f"Book: {book_info['title']} by {book_info['author']}")
            else:
                    child.display(indent + 2)    
            
# Exemplo de uso
root = BookCategory("0", "Library")

fiction = BookCategory("1", "Fiction", root)
non_fiction = BookCategory("2", "Non-Fiction", root)

root.add_sub_category(fiction)
root.add_sub_category(non_fiction)

sci_fi = BookCategory("3", "Sci-Fi", fiction)
mystery = BookCategory("4", "Mystery", fiction)

fiction.add_sub_category(sci_fi)
fiction.add_sub_category(mystery)

book1 = Book("1", "Dune", "Frank Herbert", "Sci-Fi", "Publisher One", "1965", True)
book2 = Book("2", "The Hound of the Baskervilles", "Arthur Conan Doyle", "Mystery", "Publisher Two", "1902", True)

sci_fi.add(book1)
mystery.add(book2)

root.display()    
    
    

    
    
