[10:54 am, 13/01/2025] Keffe Latte: // Private,Public Keyword
class siswa{
    String name; //Default
    public int kelas; //public
    private int nilai;
    siswa( String name, int kelas, int nilai ){
        this.name = name;
        this.kelas = kelas;
        this.nilai = nilai;
    }
    
    void Display(){
        System.out.println("Nilai : " + this.nilai);
    }
}
public class App {
    public static void main(String[] args) throws Exception {
        //DEFAULT
        siswa S001 = new siswa("Agus", 10, 100);
        System.out.println("Siswa : " + S001.name); // bisa dibaca
        S001.name = "Budi";
        System.out.println("Siswa : " + S001.name); // bisa di baca
        S001.Display();
        //PUBLIC
        siswa S002 = new siswa("Aldo", 10, 90);
        System.out.println…
[11:15 am, 13/01/2025] Keffe Latte: // Private,Public Keyword
class siswa{
    String name; //Default
    public int kelas; //public
    private int nilai;
    siswa( String name, int kelas, int nilai ){
        this.name = name;
        this.kelas = kelas;
        this.nilai = nilai;
    }
    
    void Display(){
        System.out.println("Nilai : " + this.nilai);
    }
    public void Tambahkelas(){
        this.kelas += 1;
    }
    private void Tambahnilai(){
        this.nilai += 10;
    }
}
public class App {
    public static void main(String[] args) throws Exception {
        //DEFAULT
        siswa S001 = new siswa("Agus", 10, 100);
        System.out.println("Siswa : " + S001.name); // bisa dibaca
        S001.name = "Budi";
        System.out.println("Siswa : " + S001.name); // bisa di baca
        S001.Display();
        System.out.println("--------------------------------");
        //PUBLIC
        siswa S002 = new siswa("Aldo", 10, 90);
        System.out.println("Kelas : " + S002.kelas); // bisa dibaca
        S002.name = "Nelshen";
        System.out.println("Siswa : " + S002.kelas); // bisa di baca
        S002.Tambahkelas();
        System.out.println("Kelas : " + S002.kelas);
        System.out.println("--------------------------------");
        //PRIVATE
        siswa S003 = new siswa("Martin", 11, 50);
        //System.out.println("Nilai "+ S003.nilai);
        S003.Display();
        //S003.Tambahnilai // tidak tampil
    }
}