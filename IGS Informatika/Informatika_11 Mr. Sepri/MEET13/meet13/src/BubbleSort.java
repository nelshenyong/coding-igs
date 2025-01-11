public class BubbleSort {

    public static void bubbleSortASC(int[] ar) {
        for (int j = 0; j < ar.length - 1; j++) {
            for (int i = 0; i < ar.length - 1; i++) {
                if (ar[i] > ar[i + 1]) {
                    int temp = ar[i];
                    ar[i] = ar[i + 1];
                    ar[i + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] array = {5, 3, 8, 4, 2};
        bubbleSortASC(array);
        
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}