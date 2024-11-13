class KepalaSekolah {
    String nama = "Budi";
    static void Hello() {
        System.out.println("hallo saya... kepsek");
    }
    static void Biodata(String alamat, int umur) {
        System.out.println("Alamat di " + alamat + " usia = " + umur);
    }
}

class guru extends KepalaSekolah {
    static void Hello() {
        System.out.println("Hallo saya... guru");
    }
    static void Biodata(String alamat, int umur) {
        System.out.println("Alamat guru di " + alamat + " usia = " + umur);
    }
    void superHallo() {
        super.Hello();
    }
}

public class App {
    public static void main(String[] args) {
        guru guruku = new guru();
        guruku.Hello();
        System.out.println("Nama = " + guruku.nama);
        KepalaSekolah newKepsek = new KepalaSekolah();
        newKepsek.Hello();
        System.out.println("-----------------");
        guruku.Biodata("Palembang", 23);
        newKepsek.Biodata("Jakarta", 40);
    }
}
