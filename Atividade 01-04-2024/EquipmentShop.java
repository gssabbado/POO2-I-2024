import java.util.Scanner;

public class EquipmentShop {
    public void purchase() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Selecione a categoria de equipamento:");
        System.out.println("1 - Bolas");
        System.out.println("2 - Acessórios");
        System.out.println("3 - Instrumentos");

        int opcaoCategoria = scanner.nextInt();

        switch (opcaoCategoria) {
            case 1:
                buyBall();
                break;
            case 2:
                buyAccessory();
                break;
            case 3:
                buyInstrument();
                break;
            default:
                System.out.println("Opção inválida!");
                break;
        }
    }

    private void buyBall() {
        Scanner scanner = new Scanner(System.in);
        String[] balls = {"Vôlei", "Vôlei de Praia", "Beach Tennis", "Futvôlei", "Futsal", "Basquete"};

        System.out.println("Selecione a bola que deseja comprar:");

        for (int i = 0; i < balls.length; i++) {
            System.out.println((i + 1) + " - " + balls[i]);
        }

        int opcaoBola = scanner.nextInt();

        if (opcaoBola >= 1 && opcaoBola <= balls.length) {
            System.out.println("Você comprou a bola: " + balls[opcaoBola - 1]);
        } else {
            System.out.println("Opção inválida!");
        }
    }

    private void buyAccessory() {
        Scanner scanner = new Scanner(System.in);
        String[] accessories = {"Joelheira", "Cotoveleira", "Óculos", "Boné", "Garrafa", "Bombinha de ar"};

        System.out.println("Selecione o acessório que deseja comprar:");

        for (int i = 0; i < accessories.length; i++) {
            System.out.println((i + 1) + " - " + accessories[i]);
        }

        int opcaoAcessorio = scanner.nextInt();

        if (opcaoAcessorio >= 1 && opcaoAcessorio <= accessories.length) {
            System.out.println("Você comprou o acessório: " + accessories[opcaoAcessorio - 1]);
        } else {
            System.out.println("Opção inválida!");
        }
    }

    private void buyInstrument() {
        Scanner scanner = new Scanner(System.in);
        String[] instruments = {"Rede", "Raquete"};

        System.out.println("Selecione o instrumento que deseja comprar:");

        for (int i = 0; i < instruments.length; i++) {
            System.out.println((i + 1) + " - " + instruments[i]);
        }

        int opcaoInstrumento = scanner.nextInt();

        if (opcaoInstrumento >= 1 && opcaoInstrumento <= instruments.length) {
            System.out.println("Você comprou o instrumento: " + instruments[opcaoInstrumento - 1]);
        } else {
            System.out.println("Opção inválida!");
        }
    }
}
