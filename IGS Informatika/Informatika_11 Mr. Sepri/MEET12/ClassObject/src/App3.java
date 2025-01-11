class Siswa {
    String nama;
    int nis;
    // member object
    BahasaAsing basing;

    Siswa(String nama, int nis) {
        this.nama = nama;
        this.nis = nis;
        System.out.println("nama1 = " + this.nama + " nama2 = " + nama);
    }

    void tampil(){
        System.out.println("Nama saya " + nama + " dengan nis " + nis);
    }

    void gantiNama(String nama){
        this.nama = nama; 
    }

    String tampilNama() {
        return this.nama;
    }

    String sapa(String kata) {
        return kata + " untuk nama : " + this.nama;
    }

    void pilihBahasaAsing(BahasaAsing basing) {
        this.basing = basing;
    }

    void tampilBahasaAsing() {
        System.out.println("Pilihan Bahasa Asing " + this.nama + " : " + this.basing.Basing);
    }
}

class BahasaAsing {
    String Basing;

    BahasaAsing(String Basing) {
        this.Basing = Basing;
    }

    void tampil() {
        System.out.println("Pilihan Bahasa Asing : " + Basing);
    }
}
public class App3 {
    public static void main(String[] args) {
        Siswa siswa01 = new Siswa("Budi", 1234);
        Siswa siswa02 = new Siswa("Martin", 4321);
        siswa01.tampil();
        siswa01.gantiNama("Felix");
        siswa01.tampil();
        System.out.println("tampilNama: " + siswa02.tampilNama());
        System.out.println("sapa: " + siswa02.sapa("Heiii... "));
        BahasaAsing PilihCoding = new BahasaAsing("Coding");
        BahasaAsing PilihJepang = new BahasaAsing("Jepang");
        BahasaAsing PilihMandarin = new BahasaAsing("Mandarin");
        PilihJepang.tampil();
        siswa01.pilihBahasaAsing(PilihCoding);
        siswa01.basing.tampil();
    }
}

// Buatkan sebuah class pelanggandan satu class lagi minuman dan ada class lagi makanan ceritanya nanti pelanggan dapat memilih satu object di makanan dan minuman sama seperti kode diatas dan untuk makanan dan minuman memiliki nama makanan dan minuman dan harga, serta pelanggan memiiki parameter nama dan uangnya, serta tambahkan total bayar dan sisa uang (uang - total belanja)

// template code: 
// class pelanggan {

// }

// class makanan {

// }

// class minuman {

// }

// public class app {
//     Pelanggan pelanggan1 = new Pelanggan("Budi"), 20000);
//     Makanan mie = new Makanan("Mie Instan", 10000);
//     Makanan ayam = new Makanan("Ayam Goreng", 15000);
//     Minuman air = new Minuman("Air Panas", 5000);

//     pelanggan1.pilihMakanan(mie);
//     pelanggan1.pilihMinuman(air);

//     pelanggan1.tampil();
// }
