import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        Scanner Inputan = new Scanner(System.in);
        System.out.println("Nilai = ");
        int nilai = Inputan.nextInt();
        String status;
        if(nilai >= 90){
            status = "Berhasil!! ";
        } else { status = "Gagal!! ";}

        System.out.println("Status = " + status);
        System.out.println("______________ TERNARY : ");
        status = nilai >= 95 ? "Berhasil!" : "Gagal!";
        System.out.println("Status = " + status);
    }
}