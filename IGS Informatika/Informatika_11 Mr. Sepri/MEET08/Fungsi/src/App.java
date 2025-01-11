public class App {
    public static void main(String[] args) {
        System.out.println("__________ Method / Fungsi : Void");
        Tampil();
        Tampil();
        System.out.println("__________ Method : Void - Parameter");
        Bio("DAYAT", "XI IPA 4", "PALEMBANG");

        System.out.println("__________ Method : Return - Parameter");
        System.out.println("Hasil Tambah 5 + 7 = " + (tambah(5, 7)));
        System.out.println("Hasil Rumusku = " + (rumusku(5, 7)));

    }

    private static void Tampil() {
        System.out.println("Halo Dunia!");
    }

    private static void Bio(String nama, String kelas, String alamat) {
        System.out.println("Nama: " + nama);
        System.out.println("Kelas: " + kelas);
        System.out.println("Alamat: " + alamat);
    }

    private static int tambah(int x, int y) {
        return x + y;
    }

    private static int rumusku(int x, int y) {
        int hasil = x + y + x * y;
        return hasil;
    }
}