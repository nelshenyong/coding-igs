class Sorting {
    int[] numbers = {8, 9, 10, 1, 3, 4, 11, 15, 100, 55, 2, 5, 200};

    void printArray(int[] arr) {
        for (int num : arr) System.out.print(num + " ");
        System.out.println();
    }
}

class QuickSort extends Sorting {
    void sort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }
    
    int partition(int[] arr, int low, int high) {
        int pivot = arr[high], i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        return i + 1;
    }
}

class InsertionSort extends Sorting {
    void sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i], j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j]; j--;
            }
            arr[j + 1] = key;
        }
    }
}

public class SortingProject {
    public static void main(String[] args) {
        QuickSort qs = new QuickSort();
        InsertionSort is = new InsertionSort();
        
        int[] quickSortArr = qs.numbers.clone();
        int[] insertionSortArr = is.numbers.clone();
        
        System.out.println("QuickSort:");
        qs.sort(quickSortArr, 0, quickSortArr.length - 1);
        qs.printArray(quickSortArr);
        
        System.out.println("InsertionSort:");
        is.sort(insertionSortArr);
        is.printArray(insertionSortArr);
    }
}