import java.util.ArrayList;

interface Gunung {
    void ambilfoto();
}

interface Pantai {
    void lacaklokasi();
}

class Kota implements Gunung, Pantai {
    String nama;

    public Kota(String nama) {
        this.nama = nama;
    }

    public void lacaklokasi() {
        System.out.println(nama);
    }

    public void ambilfoto() {
        System.out.println(nama);
    }


    public String toString() {
        return "Kota: " + nama;
    }
}

public class App {
    public static void main(String[] args) {
        ArrayList<Kota> kotaList = new ArrayList<>();

        Kota palembang = new Kota("Palembang");
        Kota jambi = new Kota("Jambi");
        Kota bengkulu = new Kota("Bengkulu");

        kotaList.add(palembang);
        kotaList.add(jambi);
        kotaList.add(bengkulu);

        System.out.println("List Kota:");
        for (Kota kota : kotaList) {
            System.out.println(kota);
        }

        System.out.println("\nKota:");
        for (Kota kota : kotaList) {
            kota.ambilfoto();
            kota.lacaklokasi();
            System.out.println();
        }
    }
}