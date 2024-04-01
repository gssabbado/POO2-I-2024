
public class Main {
    public static void main(String[] args) {
        Quadra quadra1 = new Quadra("Areia", 8, true, true, 50.0);
        
        Aluguel aluguel = new Aluguel();

        aluguel.alugarQuadra(quadra1);

        UserRegistry userRegistry = new UserRegistry();
        User novoUsuario = userRegistry.registerUser();

        System.out.println("Novo usuário registrado:");
        System.out.println("Nome: " + novoUsuario.nome);
        System.out.println("Email: " + novoUsuario.email);
        System.out.println("Celular: " + novoUsuario.celular);
        System.out.println("ID: " + novoUsuario.id);

        EquipmentShop equipmentShop = new EquipmentShop();
        equipmentShop.purchase();
    }
}
