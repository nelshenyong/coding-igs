public class SelectionSort {
    public static void selectionSort(int[] ar) {
        for (int j = 0; j < ar.length - 1; j++) {
            int locSelected = j;
            
            for (int i = j + 1; i < ar.length; i++) {
                if (ar[i] < ar[locSelected]) {
                    locSelected = i;
                }
            }
            
            if (locSelected != j) {
                int temp = ar[j];
                ar[j] = ar[locSelected];
                ar[locSelected] = temp;
            }
        }
    }

    public static void printArray(int[] ar) {
        for (int i : ar) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] array = {64, 25, 12, 22, 11};
        
        System.out.println("Array sebelum diurutkan:");
        printArray(array);

        selectionSort(array);
        
        System.out.println("Array setelah diurutkan:");
        printArray(array);
    }
}
