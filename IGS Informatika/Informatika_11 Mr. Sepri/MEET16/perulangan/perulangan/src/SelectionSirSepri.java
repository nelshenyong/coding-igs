public class SelectionSirSepri {
    static void selectionSort(int[] Data) {
        System.out.println("Sebelum:");
        for (int i : Data) {
            System.out.print(i + " ");
        }

        for (int i = 0; i < Data.length - 1; i++) {
            int indexArray = i;
            for (int k = i + 1; k < Data.length; k++) {
                if (Data[indexArray] > Data[k]) {
                    indexArray = k;
                }
            }
            int temp = Data[i];
            Data[i] = Data[indexArray];
            Data[indexArray] = temp;
        }

        System.out.println("\nSesudah:");
        for (int i : Data) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    static void selectionSort(char[] Data) {
        for (int i = 0; i < Data.length - 1; i++) {
            int indexArray = i;
            for (int k = i + 1; k < Data.length; k++) {
                if (Character.compare(Data[indexArray], Data[k]) > 0) { 
                    indexArray = k;
                }
            }
            char temp = Data[i];
            Data[i] = Data[indexArray];
            Data[indexArray] = temp;
        }
    }

    static void selectionSort(String[] Data) {
        for (int i = 0; i < Data.length - 1; i++) {
            int indexArray = i;
            for (int k = i + 1; k < Data.length; k++) {
                if (Data[indexArray].compareTo(Data[k]) > 0) { 
                    indexArray = k;
                }
            }
            String temp = Data[i];
            Data[i] = Data[indexArray];
            Data[indexArray] = temp;
        }
    }

    public static void main(String[] args) {
        int[] dataA = {64, 25, 12, 22, 11};
        selectionSort(dataA);

        char[] dataB = {'d', 'b', 'a', 'e', 'c'};
        selectionSort(dataB);
        System.out.println("Sorted char: " + new String(dataB));

        String[] dataC = {"Agus", "Budi", "Andi", "Doni", "Citra"};
        selectionSort(dataC);
        System.out.println("Sorted String: " + String.join(", ", dataC));
    }
}
