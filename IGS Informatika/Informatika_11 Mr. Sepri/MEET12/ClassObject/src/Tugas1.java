class Pelanggan {
    String nama;
    int uang;
    Makanan makanan;
    Minuman minuman;

    Pelanggan(String nama, int uang) {
        this.nama = nama;
        this.uang = uang;
    }

    void pilihMakanan(Makanan makanan) {
        this.makanan = makanan;
    }

    void pilihMinuman(Minuman minuman) {
        this.minuman = minuman;
    }

    int hitungTotal() {
        return this.makanan.harga + this.minuman.harga;
    }

    int hitungSisaUang() {
        return this.uang - hitungTotal();
    }

    void tampil() {
        System.out.println("Nama Pelanggan: " + this.nama);
        System.out.println("Uang: Rp" + this.uang);
        System.out.println("Pesanan Makanan: " + this.makanan.nama + " (Rp" + this.makanan.harga + ")");
        System.out.println("Pesanan Minuman: " + this.minuman.nama + " (Rp" + this.minuman.harga + ")");
        System.out.println("Total Bayar: Rp" + hitungTotal());
        System.out.println("Sisa Uang: Rp" + hitungSisaUang());
    }
}

class Makanan {
    String nama;
    int harga;

    Makanan(String nama, int harga) {
        this.nama = nama;
        this.harga = harga;
    }

    void tampil() {
        System.out.println("Makanan: " + nama + " - Rp" + harga);
    }
}

class Minuman {
    String nama;
    int harga;

    Minuman(String nama, int harga) {
        this.nama = nama;
        this.harga = harga;
    }

    void tampil() {
        System.out.println("Minuman: " + nama + " - Rp" + harga);
    }
}

public class Tugas1 {
    public static void main(String[] args) {
        Pelanggan pelanggan1 = new Pelanggan("Budi", 20000);
        
        Makanan mie = new Makanan("Mie Instan", 10000);
        Makanan ayam = new Makanan("Ayam Goreng", 15000);
        
        Minuman air = new Minuman("Air Panas", 5000);
        Minuman teh = new Minuman("Es Teh", 3000);

        pelanggan1.pilihMakanan(mie);
        pelanggan1.pilihMinuman(air);

        pelanggan1.tampil();
    }
}