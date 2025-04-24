import java.util.*;

public class Soal42 {
    public static void main(String[] args) {
        int[] list1 = {1, 1, 35, 6, 76, -4, -98};
        ArrayList<Integer> list2 = new ArrayList<>();

        for (int item : list1) {
            if (item % 2 == 0 && item % 2 == 1) {
                list2.add(item);
            }
        }

        System.out.println("list2: " + list2);
    }
}
