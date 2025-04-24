public class Soal33 {
    public static void main(String[] args) {
        int[] list1 = {1, 35, 6, 76, -4, -98};

        int min = list1[0];

        for (int item : list1) {
            if (item < min) {
                min = item;
            }
        }

        System.out.println("Minimum value: " + min);
    }
}
