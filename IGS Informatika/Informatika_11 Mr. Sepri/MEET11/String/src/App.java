public class App {
    public static void main(String[] args) {
        //STRING
        String kelasKu = "IPA1";
        char kelasKuJuga[] = { 'I', 'P', 'A', '1'};
        System.out.println("KelasKu = "+kelasKu);
        System.out.println( kelasKuJuga );
        System.out.println("----------------------------");
        System.out.println("index -0juga : " + kelasKuJuga[0] );
        System.out.println("index -0ku : " + kelasKu.charAt(0));
        System.out.println("----------------------------");
        kelasKuJuga[3] = '2';
       // kelasKu.charAt(3) = '2'; TIDAK BISA KARENA STRING BERSIFAT IMMUTABLE(TETAP, TIDAK BOLEH DI UBAH UBAH)
        System.out.println("index -0juga : " + kelasKuJuga[0] );
        System.out.println("index -0ku : " + kelasKu.charAt(0));
        System.out.println(kelasKu.substring(0, 2) + "2");
        kelasKu = kelasKu.substring(0, 3) + "2";
        System.out.println("new kelasKu="+kelasKu);
        System.out.println("----------------------------");
        String mapel = "coding";
        int alamat = System.identityHashCode(mapel);
        System.out.println("v.mapel : " + mapel + "Address : " + alamat);
        String mapel2 = "coding";
        tampilAddress(mapel2);
        String mapel3 = new String()"coding"
        String kelas = "IPA2";
        tampilAddress(kelas);
        tampilAddress(kelasKu);
        mapel = "coding123";
        tampilAddress(mapel);
    }
    private static void tampilAddress( String kata ){
        int alamat = System.identityHashCode(kata);
        System.out.println("v.mapel : " + kata + "Address : " + alamat);
    }
}