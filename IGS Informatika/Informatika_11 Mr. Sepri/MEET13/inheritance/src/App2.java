class KetuaKelas {
    String name;

    KetuaKelas(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}

class WakilKetua extends KetuaKelas {
    WakilKetua(String name) {
        super(name);
    }
}

public class App2 {
    public static void main(String[] args) {
        KetuaKelas ketua = new KetuaKelas("NelsJo");
        WakilKetua wakil = new WakilKetua("Vicko");

        System.out.println("Nama Ketua Kelas: " + ketua.getName());
        System.out.println("Nama Wakil Ketua Kelas: " + wakil.getName());
    }
}
