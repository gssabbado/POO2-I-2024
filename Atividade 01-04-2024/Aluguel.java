import java.util.Scanner;

public class Aluguel {
    public void alugarQuadra(Quadra quadra) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe a quantidade de horas para alugar a quadra:");
        int horas = scanner.nextInt();

        double totalPreco = quadra.calcularPrecoAluguel(horas);

        System.out.println("Total a pagar pelo aluguel da quadra: R$" + totalPreco);
        System.out.println("Deseja confirmar o pagamento? (true/false)");
        boolean pagamento = scanner.nextBoolean();

        if (pagamento) {
            System.out.println("Aluguel confirmado! Horas: " + horas + ", Total: R$" + totalPreco);
            quadra.marcarComoIndisponivel(); 
        } else {
            System.out.println("Aluguel cancelado.");
        }
    }
}
