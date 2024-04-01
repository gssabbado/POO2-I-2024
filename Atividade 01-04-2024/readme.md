## Sistema de Aluguel de Quadras
### Guilherme de Souza Sabbado - RA 136129
### Karen Garcia Wada - RA 163872

Este é um sistema simples para gerenciar aluguéis de quadras esportivas, registro de usuários e compra de equipamentos.
O sistema consiste em várias classes Java que implementam funcionalidades específicas.

- **Princípios de Projeto**

1. Responsabilidade Única
Cada classe tem uma responsabilidade única, o que facilita a manutenção e o entendimento do código. 
Isso permite que cada classe se concentre em uma tarefa específica sem ser sobrecarregada com funcionalidades extras.

    Em "Aluguel" a classe tem resposbilidade única relacionada ao aluguel de quadras, "UserRegestry" está relacionada ao
    registro de usuários, por fim "EquipmentShop" está relacionada a compra de equipamentos, executando apenas uma tarefa específica.

2. Segregação de Interfaces
Embora não haja interfaces explícitas neste programa, os métodos em cada classe são projetados para fornecer apenas as
funcionalidades necessárias para o contexto em que são utilizados. Isso evita que as classes dependam de métodos desnecessários.

3. Inversão de Dependências
As dependências de alto nível dependem de abstrações em vez de implementações concretas. Isso promove o desacoplamento 
entre as classes e facilita a substituição ou extensão de implementações sem afetar o código cliente.
    
    A classe "Main" é criada de modo que não seja preciso se preocupar com as implementaç~oes concretas
    dos objetos de classes "Aluguel", "UserRegistry" e "EquipmentShop". Seguindo o princípio de Inversão de 
    Dependências, afim de dependências de alto nível depedem de abstrações ao invés de implementações concretas.

4. Prefira Composição a Herança
Em vez de herdar comportamentos de outras classes, as classes neste programa têm instâncias de outras classes para usar 
seus comportamentos. Isso promove uma estrutura mais flexível e menos propensa a problemas de herança.

5. Demeter
As classes têm conhecimento limitado sobre outras classes e interagem apenas com suas classes mais próximas. 
Isso ajuda a reduzir o acoplamento e torna o código mais fácil de entender e manter.

    A Classe "Aluguel" interage apenas com esta classe para clacular o preço do aluguel e marcar a quadra como
    insisponível, isso mantem o acoplamento entre essas duas classes, seguindo o princípio de Demeter, em que 
    as classes têm conhecimento limitado sobre as outras e interagem apenas com suas classes próximas.

6. Aberto/Fechado
As classes estão abertas para extensão, mas fechadas para modificação. Isso significa que novas funcionalidades podem
ser adicionadas facilmente sem modificar as classes existentes, seguindo o princípio do Open/Closed.

7. Substituição de Liskov
Embora não haja hierarquia de classes complexa neste programa, as classes são projetadas para que as subclasses 
possam ser usadas no lugar de suas classes base sem alterar o comportamento esperado.

- **Estrutura do Projeto**

- `Main.java`: Contém o ponto de entrada do programa, onde as instâncias das classes são criadas e os métodos são chamados.
- `Aluguel.java`: Responsável por gerenciar o aluguel de quadras esportivas.
- `Quadra.java`: Define a estrutura e comportamento das quadras esportivas.
- `User.java`: Representa um usuário do sistema.
- `UserRegistry.java`: Lida com o registro de novos usuários.
- `Equipamentos.java`: Gerencia a compra de equipamentos esportivos.
