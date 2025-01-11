import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1, num2, result = 0;

        System.out.println("Pilih mode (1: Aritmatika, 2: Geometri): ");
        int mode = scanner.nextInt();

        if (mode == 1) {
            System.out.println("Masukkan angka pertama: ");
            num1 = scanner.nextDouble();

            System.out.println("Pilih operator (1: +, 2: -, 3: *, 4: /): ");
            int operator = scanner.nextInt();

            System.out.println("Masukkan angka kedua: ");
            num2 = scanner.nextDouble();

            if (operator == 1) {
                result = num1 + num2;
            } else if (operator == 2) {
                result = num1 - num2;
            } else if (operator == 3) {
                result = num1 * num2;
            } else if (operator == 4) {
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error! Tidak bisa membagi dengan nol.");
                    return;
                }
            } else {
                System.out.println("Pilihan tidak ada!");
                return;
            }

            System.out.println("Hasil: " + result);
        } else if (mode == 2) {
            System.out.println("Pilih bentuk geometri (1: Persegi, 2: Segitiga, 3: Lingkaran): ");
            int shape = scanner.nextInt();

            if (shape == 1) {
                System.out.println("Masukkan panjang sisi persegi: ");
                num1 = scanner.nextDouble();
                result = num1 * num1;
                System.out.println("Luas Persegi: " + result);
                
                for (int i = 0; i < (int) num1; i++) {
                    for (int j = 0; j < (int) num1; j++) {
                        System.out.print("* ");
                    }
                    System.out.println();
                }
            } else if (shape == 2) {
                System.out.println("Masukkan alas segitiga: ");
                num1 = scanner.nextDouble();
                
                System.out.println("Masukkan tinggi segitiga: ");
                num2 = scanner.nextDouble();

                result = 0.5 * num1 * num2;
                System.out.println("Luas Segitiga: " + result);
                
                for (int i = 1; i <= (int) num2; i++) {
                    for (int j = 1; j <= i; j++) {
                        System.out.print("* ");
                    }
                    System.out.println();
                }

            } else if (shape == 3) {
                System.out.println("Masukkan jari-jari lingkaran: ");
                num1 = scanner.nextDouble();

                result = Math.PI * num1 * num1;
                System.out.println("Luas Lingkaran: " + result);

                int r = (int) num1;
                for (int i = -r; i <= r; i++) {
                    for (int j = -r; j <= r; j++) {
                        if (i * i + j * j <= r * r) {
                            System.out.print("* ");
                        } else {
                            System.out.print("  ");
                        }
                    }
                    System.out.println();
                }
            } else {
                System.out.println("Pilihan tidak ada!");
            }
        } else {
            System.out.println("Pilihan tidak ada!");
        }
    }
}
