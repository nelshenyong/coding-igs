public class App {
    public static void main(String[] args) {
        System.out.println("Soal 1: Menampilkan deretan angka 1 sampai 10 pakai rekursif");
        cetakDeretan(1, 10);
        System.out.println("\n");

        System.out.println("Soal 2: Membalikkan angka 1234 jadi 4321");
        System.out.println(balikAngka(1234, 0));
        System.out.println();

        System.out.println("Soal 3: Menghitung faktorial dari 5");
        System.out.println(hitungFaktorial(5));
        System.out.println();

        System.out.println("Soal 4: Menampilkan 10 angka pertama deret Fibonacci");
        for (int i = 0; i < 10; i++) {
            System.out.print(deretFibonacci(i) + " ");
        }
        System.out.println("\n");

        System.out.println("Soal 5: Menampilkan 6 baris pertama Segitiga Pascal");
        cetakSegitigaPascal(6);
        System.out.println();

        System.out.println("Soal 6: Menghitung jumlah dari 1 sampai 8");
        System.out.println("Jumlah dari 1 sampai 8 adalah: " + hitungJumlah(8));
    } 

    // Soal 1
    public static void cetakDeretan(int awal, int akhir) {
        if (awal <= akhir) {
            System.out.print(awal + " ");
            cetakDeretan(awal + 1, akhir);
        }
    }

    // Soal 2
    public static int balikAngka(int angka, int hasil) {
        if (angka == 0) {
            return hasil;
        }
        return balikAngka(angka / 10, hasil * 10 + angka % 10);
    }

    // Soal 3
    public static int hitungFaktorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * hitungFaktorial(n - 1);
    }

    // Soal 4
    public static int deretFibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return deretFibonacci(n - 1) + deretFibonacci(n - 2);
    }

    // Soal 5
    public static void cetakSegitigaPascal(int baris) {
        for (int i = 0; i < baris; i++) {
            for (int spasi = baris; spasi > i + 1; spasi--) {
                System.out.print("  ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.printf("%4d", hitungNilaiPascal(i, j));
            }
            System.out.println();
        }
    }

    public static int hitungNilaiPascal(int baris, int kolom) {
        if (kolom == 0 || kolom == baris) {
            return 1;
        }
        return hitungNilaiPascal(baris - 1, kolom - 1) + hitungNilaiPascal(baris - 1, kolom);
    }

    // Soal 6
    public static int hitungJumlah(int n) {
        if (n == 1) {
            return 1;
        }
        return n + hitungJumlah(n - 1);
    }
}