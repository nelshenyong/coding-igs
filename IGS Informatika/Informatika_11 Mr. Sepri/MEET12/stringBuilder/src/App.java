import java.lang.StringBuilder;
public class App {
    public static void main(String[] args) {
        StringBuilder kata = new StringBuilder("INFORMATIKA");
        ket(kata);
        System.out.println("--------------------------");
        kata.append(" IPA 1 ");
        ket(kata);
        System.out.println("--------------------------");
        kata.insert(15, "Tersapat tiga puluh tujuh orang siswa di dalam kelas ini");
        ket(kata);
        System.out.println("--------------------------");
        kata.delete(0, 12);
        ket(kata);
        System.out.println("--------------------------");
        kata.setCharAt(0, 'Z');
        ket(kata);
        System.out.println("--------------------------");
        kata.replace(0, 4, "IPA 2");
        ket(kata);
        System.out.println("--------------------------");
        String katalain = kata.toString();
        Integer alamat = System.identityHashCode(katalain);
        System.out.println("kata = " + katalain + " address = " + alamat.toHexString(alamat));
    }
    private static void ket(StringBuilder kata) {
        System.out.println(" ");
        System.out.println("panjang = " + kata.length());
        System.out.println("kapasitas = " + kata.capacity());
        System.out.println(kata);
        Integer address = System.identityHashCode(kata);
        System.out.println("Kata = " + kata + " address = " + address.toHexString(address));
    }
}
