public class Player {
    //  1. variabel (name : TP, String) : private,
    // Constractor : 
    // Function : Display, : menampilkan nama
    private String name;
    public Player(String name){
        this.name = name;
    }
    public void display(){
        System.out.println("name : " + name);
    }
    public boolean equals(Object otherObject){
        if (this == otherObject){
            System.out.println("Object dengan reference sama");
            return true;
        } else if (this.getClass() == otherObject.getClass()){
            System.out.println("Object dengan class sama");
            System.out.println("reference berbeda");

            Player other = (Player) otherObject;
            if (this.name == other.name){
                System.out.println("name sama");
                return true;
            }else{
                System.out.println("name beda");
                return false;
            }
        }
        else {
            return false;
        }
    }
}