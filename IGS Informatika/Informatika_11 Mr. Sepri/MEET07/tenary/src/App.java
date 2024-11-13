import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner Inputan = new Scanner(System.in);
        System.out.println("Nilai x: ");
        int nilai = Inputan.nextInt();
        String status;
        if(nilai >= 90) {
            status = "Berhasil!";
        } else {status = "Berhasil!";}

        System.out.println("Status: " + status);
        System.out.println("___________ Ternary: ");
        status = nilai >= 95 ? "Berhasil!" : "Gagal!";
        System.out.println("Status: " + status);
    }
}
