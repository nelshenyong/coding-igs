import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        Scanner Inputan = new Scanner(System.in);

        System.out.print("Input panjang: ");
        byte p  = Inputan.nextByte();
        System.out.print("Input Lebar: ");
        byte l  = Inputan.nextByte();

        System.out.println("Luas Pesegi Panjang: " + (p * l));
        System.out.println("Keliling Persgi Panjang: " + (2 * (p * l)));

        System.out.print("Input tinggi: ");
        byte t = Inputan.nextByte();
        System.out.println("Volume balok: " + (t * (p * l)));
    }
}
