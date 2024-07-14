from Mediator.library_mediator import LibraryMediator
from Facede.library_facade import LibraryFacade
from ChainOfResponsability.handler import Handler
from ChainOfResponsability.handler_chain import UserEligibilityHandler, BookAvailabilityHandler, LoanLimitHandler
from Repository.book_repository import BookRepository
from Repository.user_repository import UserRepository
from Composite.book_category import BookCategory
from Composite.library_component import LibraryComponent
from Adapter.external_catalog import ExternalCatalog
from Adapter.external_catalog_adapter import ExternalCatalogAdapter
from Composite.book import Book
from User.user import User
from User.student_user import StudentUserType
from User.teacher_user import TeacherUserType
from User.admin_user import AdminUserType
from Observer.book_availability_notifier import BookAvailabilityNotifier

    # Inicializando o repositório de livros
book_repo = BookRepository()

    # Criando o mediador da biblioteca
library_mediator = LibraryMediator(book_repo)

    # Criando o facade da biblioteca
library_facade = LibraryFacade(library_mediator)

    # Criando usuários de exemplo
student = StudentUserType("Alice", "1", "123456789", "alice@example.com")
teacher = TeacherUserType("Bob", "2", "987654321", "bob@example.com")
admin = AdminUserType("Admin", "admin", "000000000", "admin@example.com")

    # Adicionando livros ao repositório (exemplo)
book_repo.add_book(Book("1", "Python Programming", "Guido van Rossum", "Programming", "TechBooks", "2023", True))
book_repo.add_book(Book("2", "Data Science Handbook", "Jake VanderPlas", "Data Science", "DataBooks", "2022", True))
book_repo.add_book(Book("3", "Design Patterns", "Erich Gamma", "Software Engineering", "DesignBooks", "2021", True))

notifier = BookAvailabilityNotifier()
user_repo = UserRepository(notifier)

admin.add_user_to_repo(user_repo, teacher)
admin.add_user_to_repo(user_repo, student)

teacher.borrow_book(book_repo, "1")
teacher.return_book(book_repo, "1")

    # Exemplo de interação com o facade
'''library_facade.borrow_book(student, "1")
library_facade.borrow_book(student, "4")  # Tentativa de empréstimo de um livro não existente

library_facade.consult_book("2")
library_facade.return_book(student, "1")
library_facade.reserve_book(teacher, "2")  # Apenas professores podem reservar livros

    # Consulta do histórico e pontuação do usuário
library_facade.consult_user_history(student)
library_facade.consult_user_score(student)'''

''' #### Teste do Mediator #####
    # Inicializando o repositório de livros
book_repo = BookRepository()

    # Criando um mediador de biblioteca com o repositório de livros
library_mediator = LibraryMediator(book_repo)

    # Criando usuários de exemplo
student = StudentUserType("Alice", "1", "123456789", "alice@example.com")
teacher = TeacherUserType("Bob", "2", "987654321", "bob@example.com")
admin = AdminUserType("Admin", "admin", "000000000", "admin@example.com")

    # Adicionando livros ao repositório (exemplo)
book_repo.add_book(Book("1", "Python Programming", "Guido van Rossum", "Programming", "TechBooks", "2023", True))
book_repo.add_book(Book("2", "Data Science Handbook", "Jake VanderPlas", "Data Science", "DataBooks", "2022", True))
book_repo.add_book(Book("3", "Design Patterns", "Erich Gamma", "Software Engineering", "DesignBooks", "2021", True))

    # Exemplo de interação com o mediador
library_mediator.borrow_book(student, "1")
library_mediator.borrow_book(student, "3")  # Tentativa de empréstimo de um livro não existente

library_mediator.consult_book("2")
library_mediator.return_book(student, "1")
library_mediator.reserve_book(teacher, "2")  # Apenas professores podem reservar livros

    # Consulta do histórico e pontuação do usuário
library_mediator.consult_user_history(student)
library_mediator.consult_user_score(student)
'''

''' ##### Teste Adapter #########
# Criação do repositório de livros
book_repository = BookRepository()

# Criação do adapter
external_catalog_adapter = ExternalCatalogAdapter(book_repository)

# Adicionando um livro através do adapter
external_book = {
    "id_book": "003",
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "category": "Fiction",
    "publisher": "J.B. Lippincott & Co.",
    "year": "1960",
    "available": True
}
external_catalog_adapter.add_external_book(external_book)

# Listando livros através do adapter
books = external_catalog_adapter.list_external_book()
print(books)

# Encontrando um livro através do adapter
found_book = external_catalog_adapter.find_external_book("003")
print(found_book)

# Removendo um livro através do adapter
external_catalog_adapter.remove_external_book("003")
'''



'''
### Teste do Composite - LibraryComponent - Book - BookCategory ###
# Criação de livros
book1 = Book("1", "O Cortiço", "Aluísio Azevedo", "Romance", "B. L. Garnier", "1890", True)
book2 = Book("2", "Romeu e Julieta", "Willian Shakespeare", "Tragédia", None, "1597", True)


# Criação de categorias
fiction_category = BookCategory(id_category="001", name="Fiction")
dystopian_category = BookCategory(id_category="002", name="Dystopian")

# Adicionando livros às categorias
dystopian_category.add(book1)
dystopian_category.add(book2)

# Adicionando subcategoria à categoria principal
fiction_category.add(dystopian_category)

# Exibindo a estrutura hierárquica
fiction_category.display()
'''

'''
admin1 = AdminUserType("RIKI", "A1", "9876543210", "rickrener@email.com")
estudante1 = StudentUserType("RIKI", "S1", "9876543210", "rickrener@email.com")
repo_books = BookRepository()
repo_users = UserRepository()
livro1 = Book("1", "O Cortiço", "Aluísio Azevedo", "Romance", "B. L. Garnier", "1890", True)
livro2 = Book("2", "Romeu e Julieta", "Willian Shakespeare", "Tragédia", None, "1597", True)


###TESTE ADMIN###
admin1.add_user_to_repo(repo_users, estudante1)
admin1.add_user_to_repo(repo_users, admin1)
'''

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