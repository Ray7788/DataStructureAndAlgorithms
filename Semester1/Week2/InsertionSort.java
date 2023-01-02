package Semester1.Week2;

// O(n²) 是插入排序！！ 不是查找！
// In other words, the book is saying "the worst case running time of insertion sort is at least cn²" i.e, in the worst case it would not run better than cn².
// (Similarly, worst case is O(n²) means that the worst running time is at most c2 n², ie. would not run worse than c2 n²
// in which, since the worst case is O(n²) and Ω(n²), the strict bound is n², denoted as θ(n²))

public class InsertionSort {
    public void search(int[] A, int n){
        for(int i = 2; i < n; i++){
            int key = A[i];
            int j = i -1;

            while(j > 0 && A[j] > key){
                A[j+1] = A[j];
                j -= 1;
            }

            A[j+1] = key;
        }
    }
}
