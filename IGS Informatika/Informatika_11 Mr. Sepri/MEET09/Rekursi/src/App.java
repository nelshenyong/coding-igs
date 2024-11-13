import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner Inputan = new Scanner(System.in);
        System.out.println("Enter Nilai = ");
        int nilai = Inputan.nextInt();

        TampilNilai(nilai);
        TampilNilai(nilai);
        int hasilTambahNilai = TambahNilai(nilai);
        System.out.println("Hasil Fungsi Tambah = " + hasilTambahNilai);

        int hasilFaktorial = Faktorial(nilai);
        System.out.println("Hasil Faktorial " + hasilFaktorial);
    }
    private static void TampilNilai ( int parameter) {
        System.out.println("Nilai = " + parameter);
        if (parameter == 0) {
            return;
        }
        parameter--;
        TampilNilai(parameter);//Rekursi..
    }
    private static int TambahNilai(int parameter ) { 
        System.out.println("Nilai fungsi(TambahNilai) "+ parameter);
        if ( parameter == 0 ){
            return parameter;
        }
        parameter--;
        return parameter + TambahNilai(parameter - 1);// Rekursi
        
    }
    private static int Faktorial(int parameter ) { 
        System.out.println("Nilai fungsi(TambahNilai) "+ parameter);
        if ( parameter == 1 ){
            return parameter;
        }
        return parameter * Faktorial(parameter - 1);// Rekursi
        
    }
}
