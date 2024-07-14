from book_repository import BookRepository
from user_repository import UserRepository
from book import Book
from user import User
from student_user import StudentUserType
from teacher_user import TeacherUserType
from admin_user import AdminUserType

admin1 = AdminUserType("RIKI", "A1", "9876543210", "rickrener@email.com")
estudante1 = StudentUserType("RIKI", "S1", "9876543210", "rickrener@email.com")
repo_books = BookRepository()
repo_users = UserRepository()
livro1 = Book("1", "O Cortiço", "Aluísio Azevedo", "Romance", "B. L. Garnier", "1890", True)
livro2 = Book("2", "Romeu e Julieta", "Willian Shakespeare", "Tragédia", None, "1597", True)


###TESTE ADMIN###
admin1.add_user_to_repo(repo_users, estudante1)
admin1.add_user_to_repo(repo_users, admin1)

#admin1.uptade_score(repo_users, "S1", -2)
#admin1.consult_history_of_user(repo_users,"S1")
#admin1.consult_score_of_user(repo_users, "S1")
#admin1.find_user(repo_users, "A1")
#print("Removendo...")
#admin1.remove_user(repo_users, "A1")
#admin1.add_book_to_repo(repo_books, livro1) #Imprime "Book registered! , ID: id"
#admin1.add_book_to_repo(repo_books, livro2)

#repo_books.list_books() #Retorna a lista dos livros com todas suas informações
#repo_users.list_users() #Tem como deixar bonito, mas assim ta funcionando
#admin1.reserve_book(repo_books, "1")
#admin1.reserve_book(repo_books, "1")
#admin1.reserve_book(repo_books, "5")
#print("Procurando")
#admin1.find_user(repo_users, "A1")
#admin1.find_user(repo_users, "KKKK")

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