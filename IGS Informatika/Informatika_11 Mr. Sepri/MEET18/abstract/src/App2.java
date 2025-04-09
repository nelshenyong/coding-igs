

// Nama: Nelshen Yong
abstract class BangunDatar {
    abstract double luas();
}

class Lingkaran extends BangunDatar {
    private double jari_jari;

    Lingkaran(double jari_jari) {
        this.jari_jari = jari_jari;
    }

    double luas() {
        return Math.PI * jari_jari * jari_jari;
    }
}

class Segitiga extends BangunDatar {
    private double alas;
    private double tinggi;

    Segitiga(double alas, double tinggi) {
        this.alas = alas;
        this.tinggi = tinggi;
    }

    double luas() {
        return 0.5 * alas * tinggi;
    }
}

public class App2 {
    public static void main(String[] args) throws Exception {
        Lingkaran lingkaran = new Lingkaran(7);
        Segitiga segitiga = new Segitiga(5, 6);

        System.out.println("Luas lingkaran: " + lingkaran.luas());
        System.out.println("Luas segitiga: " + segitiga.luas());
    }
}