public class App {
    public static void main(String[] args) {
        byte a = 100;
        boolean nilai1 = a > 10 && a < 15;
        boolean nilai2 = a > 13 && a < 20;
        boolean nilai3 = a > 20 && a < 30;

        boolean hasil = nilai1 && nilai2 || nilai3;
        System.out.println(hasil);
    }
}
