class BubbleSortAsc {
     BubbleSortAsc (int data[]) {
        for (int k = 0; k < data.length - 1; k++) {
            for (int i = 0; i < data.length - 1; i++) {
                int newData = data[i];
                if (data[i] > data[i + 1]) {
                    data[i] = data[i + 1];
                    data[i + 1] = newData;
                }
            }
        }

        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i]);
        }
    }

    BubbleSortAsc (String data[]) {
        for (int k = 0; k < data.length - 1; k++) {
            for (int i = 0; i < data.length - 1; i++) {
                int newData = data[i];
                if (data[i].compareTo(data[i + 1]) > 0) {
                    data[i] = data[i + 1];
                    data[i + 1] = newData;
                }
            }
        }

        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i]);
        }
    }
}

public class App { 
    public static void main(String[] args) {
        int data[] = {5, 3, 8, 4, 2};
        BubbleSortAsc obj1 = new BubbleSortAsc(data);
        System.out.println("\n");
        Strict[] data1 = {"bebek", "ayam", "kambing", "sapi", "kuda"};
        BubbleSortAsc obj2 = new BubbleSortAsc(data1);
        // String kata1 = "abc"; // -
        // String kata2 = "zdf"; // +
        // System.out.println(kata1.compareTo(kata2));
        // char huruf1 = 'a';
        // char huruf2 = 'b';
        // System.out.println(huruf1 - huruf2);
    }
}