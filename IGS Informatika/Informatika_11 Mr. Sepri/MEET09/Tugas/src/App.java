    import java.util.Scanner;

    public class App{
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            
            System.out.print("Masukkan panjang: ");
            int panjang = scanner.nextInt();

            
            System.out.print("Masukkan lebar: ");
            int lebar = scanner.nextInt();

            
            System.out.print("Pilih (Luas/Keliling): ");
            String pilihan = scanner.next();

            if (pilihan.equalsIgnoreCase("keliling")) {
                
                int keliling = 2 * (panjang + lebar);
                System.out.println("Keliling persegi panjang adalah: " + keliling);
            } else if (pilihan.equalsIgnoreCase("luas")) {
            
                int luas = panjang * lebar;
                System.out.println("Luas persegi panjang adalah: " + luas);
            } else {
                System.out.println("Error ! Pilihan Salah !");
            }

            scanner.close();
        }
    }
