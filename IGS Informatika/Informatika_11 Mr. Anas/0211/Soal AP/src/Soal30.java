import java.util.Scanner;

public class Soal30 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number (a): ");
        int a = scanner.nextInt();
        System.out.print("Enter second number (b): ");
        int b = scanner.nextInt();

        if (a % 3 == 0 && b % 3 == 0) {
            System.out.println("TRUE");
        } else {
            System.out.println("FALSE");
        }

        scanner.close();
    }
}
