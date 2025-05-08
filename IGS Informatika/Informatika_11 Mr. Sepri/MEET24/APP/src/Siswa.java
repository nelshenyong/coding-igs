public class Siswa {
    private String nama;
    Siswa (String nama){
        this.nama = nama;
    }

    public String getNama(){
        return this.nama;
    }

    public void setNama(String newNama){
        this.nama = newNama;
    }

    public String toString(){
        return "nama: " + nama;
    }
}