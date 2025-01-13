// OVERRIDING :
class Provinsi {
    String name;
    void Display() {
        System.out.println("Ini adalah provinsi : " + name);
    }
}
class kota extends Provinsi {
    void Display(){
        System.out.println("Ini adalah kota : " + name);
    }   
}
public class App {
    public static void main(String[] args) throws Exception {
        Provinsi sumsel = new Provinsi();
        sumsel.name = "Sumatera Selatan";
        sumsel.Display();

        kota plg = new kota();
        plg.name = "Palemmbang";
        plg.Display();
    }
}