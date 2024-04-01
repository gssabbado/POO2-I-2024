import java.util.Scanner;

public class UserRegistry {
    public User registerUser() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o nome:");
        String nome = scanner.nextLine();

        System.out.println("Informe o email:");
        String email = scanner.nextLine();

        System.out.println("Informe o celular:");
        String celular = scanner.nextLine();

        System.out.println("Informe o ID:");
        String id = scanner.nextLine();

        User newUser = new User(nome, email, celular, id);
        System.out.println("Usuário registrado com sucesso!");

        return newUser;
    }
}
