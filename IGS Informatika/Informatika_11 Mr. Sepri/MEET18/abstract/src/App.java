abstract class myBio{
    protected String name;
    void heii(){
        System.out.println("Hello " + name);
    }
    abstract void woii();
    abstract String gantiNama(String name);
}

class mySelf extends myBio{
    mySelf(String name){
        this.name = name;
    }
    void woii(){System.out.println("woi " + name);}
    String gantiNama(String name){
        return this.name = name;
    }
}

public class App {
    public static void main(String[] args) throws Exception {
       mySelf me = new mySelf("John");
       me.heii();
       me.gantiNama("bima");
        me.woii();
    }
}