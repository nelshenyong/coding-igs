public class App {
    public static void main(String[] args) throws Exception {
        Player player1 = new Player("budi");
        player1.display();

        Object player2 = player1;
        String player1_ = player1.toString();
        String player2_ = player1.toString();
        System.out.println("String Player1 = "+player1_);
        System.out.println("String Player2 = "+player2_);
        Object Player3 = new Player("asep");
        System.out.println("String Player3 = "+Player3.toString());

        Player player4 = new Player("Santoso");
        Player player5 = new Player("Santosi");

        System.out.println("----------------------------");
        System.out.println(player1.equals(player2));
        System.out.println("----------------------------");
        System.out.println(player1.equals(Player3));
        System.out.println("----------------------------");
        System.out.println(player4.equals(player5));
        System.out.println(player4.equals("jaja"));
        

    }
}