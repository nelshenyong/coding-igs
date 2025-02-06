class data {
    public int dataIntPub;
    private int dataIntPriv;

    data() {
        dataIntPriv = 10;
        dataIntPub = 20;
    }

    // SETTER
    public int SetdataIntPriv() {
        return this.dataIntPriv;
    }
    // GETTER
    void SetdataIntPriv(int dataIntPriv) {
        this.dataIntPriv = dataIntPriv;
    }
}

public class App {
    public static void main(String[] args) throws Exception {
        data Obj = new data();
        System.out.println("1 Data public = " + Obj.dataIntPub);
        Obj.dataIntPub = 15;
        System.out.println("2 Data public = " + Obj.dataIntPub);
        System.out.println("3 Data private = " + Obj.SetdataIntPriv());
        Obj.SetdataIntPriv(10);
        System.out.println("4 Data private = " + Obj.SetdataIntPriv());
    }
}
