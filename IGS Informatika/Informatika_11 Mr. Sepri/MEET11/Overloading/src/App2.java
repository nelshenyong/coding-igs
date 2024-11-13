import java.util.Scanner;

public class App2 {
    public static void main(String[] args) throws Exception {
        // OVERLOAD
        Scanner Inputan = new Scanner(System.in);
        System.out.println("Enter Panjang : ");
        int Panjang = Inputan.nextInt();
        System.out.println("Enter Lebar : ");
        int Lebar = Inputan.nextInt();
        System.out.println("Enter Sisi : ");
        int s = Inputan.nextInt();
        System.out.println("-----------------------------");
        keliling(Panjang, Lebar);
        luas(Panjang, Lebar);
        System.out.println("-----------------------------");
        float Panjangf = 5.5f;
        float Lebarf = 7.2f;
        System.out.println("--------------------------");
        keliling(Panjangf, Lebarf);
        luas(Panjangf, Lebarf);
        System.out.println("luas (Float) : "+ (luas(Panjangf, Lebarf)));
        System.out.println("luas (Int): "+ (luas(Panjang, Lebar)));
        keliling(s);
        luas(s);


    }
    private static void keliling (int p , int l){
        System.out.println("Keliling Lingkaran (Int) : " + ((2*p )+ (2*l)));
    }
    // syarat overloading parameter func berbeda (Tipe data/jml param)
    private static void keliling (float p , float l){
        System.out.println("Keliling Lingkaran (Float) : " + ((2*p )+ (2*l)));
    }
    private static int luas(int p, int l){
        return p*l;
    }
    private static float luas(float p, float l){
        return p*l;
    }
    private static void keliling (int s ){
        System.out.println("Keliling Persegi (Int) : " + (4*s));
    }
    private static void luas (int s ){
        System.out.println("Luas Persegi (Int) : " + (s*s));
    }

}