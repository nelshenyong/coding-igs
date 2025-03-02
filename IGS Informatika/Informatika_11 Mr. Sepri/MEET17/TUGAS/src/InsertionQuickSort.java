import java.util.Arrays;
import java.util.Comparator;

class DataHandler {
    protected int[] dataInt = {8, 9, 10, 1, 3, 4, 11, 15, 100, 55, 2, 5, 200};
    protected char[] dataChar = {'v', 'b', 'a', 'z', 'v', 'c', 'f'};
    protected String[] dataString = {"CODING", "kelas", "XI", "IPA", "I"};

    protected void displayData() {
        System.out.println("Integer Data: " + Arrays.toString(dataInt));
        System.out.println("Character Data: " + Arrays.toString(dataChar));
        System.out.println("String Data: " + Arrays.toString(dataString));
    }
}

class Sorting extends DataHandler {
    
    public Sorting() {
        super();
    }
    
    private void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    
    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }
    
    private void insertionSort(int[] arr, boolean ascending) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && ((ascending && arr[j] > key) || (!ascending && arr[j] < key))) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    private void sortCharArray(char[] arr, boolean ascending) {
        Arrays.sort(arr);
        if (!ascending) {
            for (int i = 0; i < arr.length / 2; i++) {
                char temp = arr[i];
                arr[i] = arr[arr.length - 1 - i];
                arr[arr.length - 1 - i] = temp;
            }
        }
    }

    private void sortStringArray(String[] arr, boolean ascending) {
        Arrays.sort(arr, ascending ? Comparator.naturalOrder() : Comparator.reverseOrder());
    }

    public void sortData() {
        System.out.println("Sorting Integer Data (Ascending using QuickSort):");
        quickSort(dataInt, 0, dataInt.length - 1);
        System.out.println(Arrays.toString(dataInt));
        
        System.out.println("Sorting Integer Data (Descending using Insertion Sort):");
        insertionSort(dataInt, false);
        System.out.println(Arrays.toString(dataInt));
        
        System.out.println("Sorting Character Data (Ascending):");
        sortCharArray(dataChar, true);
        System.out.println(Arrays.toString(dataChar));
        
        System.out.println("Sorting Character Data (Descending):");
        sortCharArray(dataChar, false);
        System.out.println(Arrays.toString(dataChar));
        
        System.out.println("Sorting String Data (Ascending):");
        sortStringArray(dataString, true);
        System.out.println(Arrays.toString(dataString));
        
        System.out.println("Sorting String Data (Descending):");
        sortStringArray(dataString, false);
        System.out.println(Arrays.toString(dataString));
    }
}

public class InsertionQuickSort {
    public static void main(String[] args) {
        Sorting sorting = new Sorting();
        sorting.displayData();
        sorting.sortData();
    }
}