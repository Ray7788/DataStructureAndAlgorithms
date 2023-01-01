package Semester1.Week2;

// O(n²) 是插入排序！！ 不是查找！
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
