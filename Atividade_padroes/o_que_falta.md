# Atualização das 6h
(É interessante colocar as mensagnes em uma classe, massó se tiver tempo)



- Fiz os seguintes designs:
    1. Composite;
    2. Adapter;
    3. Mediator;
    4. Chain of Resposability;
    5. Facade;

- Faltam os seguintes designs:
    - Observer ;
    - Singleton;

- Atualizei alguns atributos e métodos de outros arquivos:
    1. BookCategory
        * tirei os métodos de sub_category (add e get), visto que com o get children ja deva fazer isso, além do teste do composite.
    
    2. Book
        * Foi alterado o 'object' por 'LibraryComponent' na classe;
        * Arrumei o erro de gramática de 'set_book_availalability' para 'set_book_availability'
        * E foi adicionado mais métodos como add, remove e display
    
    3. Users (geral)
        * O método is_eligible() é para ver se o usuário é elegivel baseado no seu score (é bom definir se score alto é bom ou ruim);
        * o método can_borrow_more_books() épara ver se o usuário ja atingiu o limite máximo de livros emprestados.
        * Cada tipo de usuário tem uma condição um pouco mais diferente, o admin pode pegar tudo e está sempre elegivel. 

- Não cheguei a atualizar tudo da UML, principalmente em relação aos atributos e métodos.

## Observações
Eu deixei alguns testes de cada design na main, é bom refazer e ver se faltou algum teste para ser feito.

Não esqueça de sincronizar o fork no site do github, no teu repositório.

Perdão se deixei algo para trás.

Se der muito problema, da pra pegar o código mais antigo.


### Composite:
 * Os arquivos dele (estão relacionados) são o **library_component**, **book** e **book_category**;
 * O seu teste está na linha 112 da main;
 * indent no display é só pra deixar a msg mais bonita;
 * O Optional pelo que eu pesquisei, seria uma forma de dizer que o objeto pode ser nada também;

### Adapter:
 * Os arquivos dele (estão relacionados) são o **book**, **external_catalog *(é uma interface)***, **external_catalog_adapter** e o **book_repository**;
 * O seu teste está na linha 78 da main;
 * Pareceu que ocorreu tudo certo;
 * É bom verificar se está bem conectado, posso ter deixado algo passar;

### Mediator e Chain of Resposability:
 * Os arquivos dele (estão relacionados) são o **library_mediator**, **handler *(é uma interface)*** e o **handler_chain *(é o que possui todos as classes)***;
 * Basicamente parei nesses dois, eles estão dando problema no caso de fazer uma tentativa de empréstimo de um livro que não existe, seu teste está na linha 17;
 * esses padrões fizeram eu ter que criar alguns métodos adicionais, como is_eligible() e can_borrow_more_books();

### Facade
 * Ele está relacionado ao mediator e seu arquivo é o **library_facade**
 * Criei rapidamente então não mexi muito nele, não possui teste (ele acaba meio que testando junto com o mediator)


