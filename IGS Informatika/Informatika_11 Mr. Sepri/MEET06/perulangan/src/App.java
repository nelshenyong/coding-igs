import java.util.Scanner;
public class App {
    public static void main(String[] args) {
        Scanner Input = new Scanner(System.in);
        
        System.out.println("number : ");
        int num = Input.nextInt();

        System.out.println("______________________ FOR LOOP");
        for(int i = 0; i < num;i++){
            System.out.print( i + " ");
        };

        System.out.println("\n_____________________ FOR WHILE");
        int i = 1;
        while (i <= num){
            System.out.println(i + " ");
            i++;
        };
        
        System.out.println("______________________ FOR DO-WHILE");
        i = 1;
        do {
            System.out.println(i + " ");
            i++;
        } while (i <= num);
        System.out.println("______________________ FOR BREAK");
        while ( i <= num){        
            System.out.println(i + " ");
            if (i == 5){
                break;
            }
            i++;}
            System.out.println("______________________ FOR CONTINUE");
            while ( i <= num){        
                System.out.println(i + " ");
                if (i == 5){
                    continue;
                }
                if ( i == 6){
                    break;
                }
                i++;}
            
        
    }
}