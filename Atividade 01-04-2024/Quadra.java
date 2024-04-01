public class Quadra {
    String tipoQuadra;
    int capacidade;
    boolean disponivel;
    boolean coberto;
    double preco;

    public Quadra(String tipoQuadra, int capacidade, boolean disponivel, boolean coberto, double preco) {
        this.tipoQuadra = tipoQuadra;
        this.capacidade = capacidade;
        this.disponivel = disponivel;
        this.coberto = coberto;
        this.preco = preco;
    }

    public double calcularPrecoAluguel(int horas) {
        return horas * this.preco;
    }

    public void marcarComoIndisponivel() {
        this.disponivel = false;
    }
}
