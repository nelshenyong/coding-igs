class Siswa {
    String nama = "Kaka";
    int nim;
    String jurusan;

    Siswa(String paramNama, int paramNim, String paramJurusan) {
        nama = paramNama;
        nim = paramNim;
        jurusan = paramJurusan;
        System.out.println("Nama saya " + nama + " dengan nim = " + nim + " sekarang ada di jurusan " + jurusan);
    }

    Siswa(String paramNama) {
        System.out.println("Namaku adalah " + paramNama + " temanku adalah " + nama);
    }

    Siswa(String nama, String jurusan) {
        nama = nama;
        jurusan = jurusan;
        System.out.println("Nama saya " + nama + " dengan jurusan " + jurusan);
    }
}

public class App2 {
    public static void main(String[] args) {
        Siswa siswa01 = new Siswa("Budi", 1234, "IPA KOMPUTER");
        Siswa siswa02 = new Siswa("Martin", 4321, "IPA KEDOKTERAN");
        Siswa siswa03 = new Siswa("Jeje");
        Siswa siswa04 = new Siswa("Lala", "IPS");
    }
} 