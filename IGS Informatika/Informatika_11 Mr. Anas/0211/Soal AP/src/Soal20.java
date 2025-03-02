public class Soal20 {
    public static void hasil(int n) {
        if (n > 10) {
            hasil(n / 10);
        }
        System.out.print(n % 10);
    }

    public static void main(String[] args) {
        hasil(347); 
    }
}
