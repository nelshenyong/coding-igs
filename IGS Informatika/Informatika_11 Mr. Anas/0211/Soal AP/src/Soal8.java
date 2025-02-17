import java.util.*;

public class Soal8 {
    public static void main(String[] args) {
        ArrayList<String> words = new ArrayList<>(Arrays.asList("Cat", "Meow", "Cow", "Moo"));
        System.out.println(mystery(words));
    }

    public static String mystery(ArrayList<String> words) {
        String a = "Friend";
        for (String item : words) {
            a += item;
        }
        a += "Friend";
        return a;
    }
}
