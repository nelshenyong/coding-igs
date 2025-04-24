import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> DataList = new ArrayList<>();
        DataList.add("Hello");
        DataList.add("World");
        System.out.println(DataList);

        Player p1 = new Player("John", 20);
        Player p2 = new Player("Jane", 25);
        A_Player p3 = new A_Player("Jono", 30);
        B_Player p4 = new B_Player("Jono", 30);

        Player[] DataPlayer = new Player[2];
        DataPlayer[0] = p1;
        DataPlayer[1] = p2;
        // DataPlayer[2] = p3;
        // DataPlayer[3] = p4;
        for (Player p : DataPlayer) {
            p.display(); 
        }

        ArrayList<Player> ListPlayer = new ArrayList<>();
        ListPlayer.add(p1);
        ListPlayer.add(p2);
        ListPlayer.add(p3);
        ListPlayer.add(p4);


        for (Player p : ListPlayer) {
            p.display(); 
        }
        System.out.println("Get 2 Player: " + ListPlayer.get(1));
        System.out.println("Ex: " + ListPlayer.indexOf(p3));
    }
}
