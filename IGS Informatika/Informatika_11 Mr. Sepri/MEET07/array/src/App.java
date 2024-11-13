public class App {
    public static void main(String[] args) {
        System.out.println("_________ Array - 1");
        String[] arrayStrings = new String[3];
        // Diatas sering disebut dengan Stack
        arrayStrings[0] = "Hendri";
        arrayStrings[1] = "Martin";
        arrayStrings[2] = "Freddy";
        System.out.println(arrayStrings);
        System.out.println("Data - 0: " + arrayStrings[0]);
        System.out.println("Data - 1: " + arrayStrings[1]);
        System.out.println("Data - 2: " + arrayStrings[2]);

        System.out.println("_________ Array - 2");
        Byte[] arrayBytes = new Byte[] {
            1, 2, 3, 4
        };
        // Diatas sering disebut Memory Heap
        System.out.println(arrayBytes);
        System.out.println("Data - 0: " + arrayBytes[0]);
        System.out.println("Data - 1: " + arrayBytes[1]);
        System.out.println("Data - 2: " + arrayBytes[2]);
        System.out.println("Data - 3: " + arrayBytes[3]);

        System.out.println("_________ Array - 3");
        int[] arrayInt = {
            4, 3, 2, 1
        };
        System.out.println("Data - 0: " + arrayInt[0]);

        System.out.println("_________ Panjang Array");
        System.out.println("Panjang arrayInt: " + arrayInt.length);

        System.out.println("_________ For Loop - Array");
        for (int i = 0; i < arrayInt.length; i++) {
            System.out.println("Data - " + (i+1) + ": " + arrayInt[i]);
        }

        System.out.println("_________ For Loop Each - Array");
        for (int i: arrayInt ) {
            System.out.println("Data: " + i);
        }

    }
}
