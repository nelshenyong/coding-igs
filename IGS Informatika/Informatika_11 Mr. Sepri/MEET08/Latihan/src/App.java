import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Panjang: ");
        int panjang = input.nextInt();
        System.out.print("Lebar: ");
        int lebar = input.nextInt();

        tampilGambar(panjang, lebar); 
        tampilKelilingDanLuas(panjang, lebar);   
    }

    private static void tampilKelilingDanLuas(int x, int y) {
        System.out.println("Luas: " + luas(x, y));
        System.out.println("Keliling: " + keliling(x, y));
    }

    private static int luas(int x, int y) {
        return x * y;
    }

    private static int keliling(int x, int y) {
        return 2 * (x + y);
    }

    private static void tampilGambar(int x, int y) {
        for (int i = 0; i < y; i++) {
            for (int j = 0; j < x; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}