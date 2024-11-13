package Informatika_11.MEET03.tantangan.tantangan.src.com;

public class App {
    public static void main(String[] args) {
        int nilai = 99; 

        boolean kondisi1 = nilai > 1 && nilai < 3;
        boolean kondisi2 = nilai > 88 && nilai < 101;
        boolean kondisi3 = nilai > 99 && nilai < 101;
        boolean hasil = kondisi1 || kondisi2 && kondisi3;

        System.out.println("Hasil: " + hasil);
    }
}