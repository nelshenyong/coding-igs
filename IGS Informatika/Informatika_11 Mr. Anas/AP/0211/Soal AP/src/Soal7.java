import java.util.*;

public class Soal7 {
    public static void main(String[] args) {
        // ArrayList seharusnya menggunakan Integer, bukan int
        ArrayList<Integer> aList = new ArrayList<Integer>(Arrays.asList(1, 1, 35, 6));
        System.out.println(aList);
        System.out.println(mystery(aList));
    }

    public static int mystery(ArrayList<Integer> aList) {
        return aList.get(0);
    }
}
