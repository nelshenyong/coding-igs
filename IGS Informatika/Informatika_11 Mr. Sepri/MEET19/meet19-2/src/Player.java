public class Player {
    private String name;
    private double health;

    Player (String name, double health) {
        this.name = name;
        this.health = health;
    }

    void setName(String new_name) {
        this.name = new_name;
    }

    void display(){
        System.out.println("name: " + this.name + " health: " + this.health);
    }
}