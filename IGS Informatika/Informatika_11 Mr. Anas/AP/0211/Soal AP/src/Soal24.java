public class Soal24 {
        public static void main(String[] args) {
            int num = 7;
    
            while (num != 6) {
                if (num % 2 == 0) {
                    System.out.println(num);
                    break;
                } else {
                    num = num + 1;
                }
            }
        }
    
}
