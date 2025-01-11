import java.util.Scanner;

public class lat1 {
    public static void main(String[] args) {
        Scanner input_shen = new Scanner(System.in);

        System.out.print("Masukkan jumlah angka yang ingin diinput: ");
        int jumlahAngka = input_shen.nextInt();

        int total = 0;
        int min = 0;
        int max = 0;
        String semuaNilai = ""; 

        for (int i = 1; i <= jumlahAngka; i++) {
            System.out.print("Nilai ke-" + i + ": ");
            int nilai = input_shen.nextInt();

            if (i == 1) {
                semuaNilai = Integer.toString(nilai);
            } else {
                semuaNilai += ", " + nilai;
            }

            total += nilai;

            if (i == 1) {
                min = nilai;
                max = nilai;
            } else {
                if (nilai < min) {
                    min = nilai;
                }

                if (nilai > max) {
                    max = nilai;
                }
            }
        }

        double rataRata = (double) total / jumlahAngka;

        long faktorial = 1;
        for (int i = 1; i <= jumlahAngka; i++) {
            faktorial *= i;
        }

        boolean isPrima = true;
        if (jumlahAngka == 1) {
            isPrima = false;
        } else {
            for (int i = 2; i < jumlahAngka; i++) {
                if (jumlahAngka % i == 0) {
                    isPrima = false;
                    break;
                }
            }
        }

        System.out.println("\nHasil:");
        System.out.println("Nilai yang diinput: " + semuaNilai);
        System.out.println("Total: " + total);
        System.out.println("Nilai Minimum: " + min);
        System.out.println("Nilai Maksimum: " + max);
        System.out.println("Rata-rata: " + rataRata);
        System.out.println("Faktorial dari " + jumlahAngka + " adalah: " + faktorial);


        if (isPrima) {
            System.out.println(jumlahAngka + " adalah bilangan prima.");
        } else {
            System.out.println(jumlahAngka + " bukan bilangan prima.");
        }
    }
}
