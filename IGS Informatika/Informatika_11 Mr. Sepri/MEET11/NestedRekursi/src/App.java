import java.util.Scanner;

public class App {
    public static void main(String[] args)  {
        Scanner Inputan = new Scanner(System.in);
        System.out.print("Enter angka : ");
        int num = Inputan.nextInt();
        System.out.println("Hasil Fib : "+ Fib(num));
    }

    private static int Fib ( int x ){
        if(x == 0 || x == 1 ){
            return x;
        }
        else {
            return Fib( x - 1 ) + Fib( x - 2 );
        }
    }
}