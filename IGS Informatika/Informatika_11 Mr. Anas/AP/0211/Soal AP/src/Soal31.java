import java.util.*;

public class Soal31 {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>(Arrays.asList(1, 4, 7, 10, 13));
        int count = 0;

        for (int i = 0; i < nums.size(); i++) {
            int index = nums.size() - count - 1;
            System.out.print(nums.get(index) + " ");
            count++;
        }
    }
}
