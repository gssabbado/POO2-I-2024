from book_repository import BookRepository
from user_repository import RepositoryUser
from book import Book
from user import User
from student_user import StudentUserType
from teacher_user import TeacherUserType
from admin_user import AdminUserType

admin1 = AdminUserType("RIKI", "A1", "9876543210", "rickrener@email.com")

estudante1 = StudentUserType("RIKI", "S1", "9876543210", "rickrener@email.com")

repo = BookRepository()

livro1 = Book("1", "O Cortiço", "Aluísio Azevedo", "Romance", "B. L. Garnier", "1890", True)
livro2 = Book("2", "Romeu e Julieta", "Willian Shakespeare", "Tragédia", None, "1597", True)



#repo.add_book("1", "teste", "lulu", "horror", "TESTE", "1999", True)
#repo.add_book("2", "atata", "elio", "gospel", "ADS", "1411", True)
admin1.add_book_to_repo(repo, "1", "O Cortiço", "Aluísio Azevedo", "Romance", "B. L. Garnier", "1890", True)
admin1.add_book_to_repo(repo, livro2)

repo.list_books()

'''
usuario._book_history = {
    "id_book": "1",
    "title": "teste",
    "author": "lulu",
    "category": "horror",
    "publisher": "TESTWE",
    "year": "1999",
}
usuario.add_books(1, "teste", "lulu", "horror", "TESTE", 1999)
usuario.add_books(2, "te", "lasadlu", "gospel", "TEeE", 1000)


usuario.consult_history()

usuario.consult_score()
'''
#666', 'Me ajuda Deus', 'Lucifer Cristo', 'Horror', 'Inferno Astral', '1994', True

'''
    def get_book(self):
        return {
                "id_book": self._id_book,
                "title": self._title,
                "author": self._author,
                "category": self._category,
                "publisher": self._publisher,
                "year": self._year,
                "available": self._available
                }'''