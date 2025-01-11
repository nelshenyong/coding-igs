class Siswa{
    String nama;
    String kelas;
    int nim;
    double nilai;
}

public class App {
    public static void main(String[] args) {
        {
            Siswa siswa01 = new Siswa();
            siswa01.nama = "Martin";
            siswa01.kelas = "IPA 6";
            siswa01.nim = 12345;
            siswa01.nilai = 100;
            System.out.println("Hai" + siswa01.nama + " saya kelas "  + siswa01.kelas + " dengan NIM " + siswa01.nim + " dengan nilai " + siswa01.nilai);   
            
            System.out.println("------------------");
            
            Siswa siswa02 = new Siswa();
            siswa02.nama = "Felix";
            siswa02.kelas = "IPA 1";
            siswa02.nim = 911;
            siswa02.nilai = 0;
            System.out.println("Hai" + siswa02.nama + " saya kelas "  + siswa02.kelas + " dengan NIM " + siswa02.nim + " dengan nilai " + siswa02.nilai);
        }
    }
}
