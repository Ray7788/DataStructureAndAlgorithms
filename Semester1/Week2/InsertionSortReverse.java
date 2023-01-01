package Semester1.Week2;

import java.util.Arrays;

// O(n²) 插入排序 （递减顺序）
public class InsertionSortReverse {
    public static void sort(int[] A){
        for(int i = 1; i < A.length; i++){
            int key = A[i];
            int j = i -1;

            while(j > 0 && A[j] < key){
                A[j+1] = A[j];
                j -= 1;
            }

            A[j+1] = key;
        }

        System.out.println(Arrays.toString(A));
    }

    public static void main(String[] args) {
        int a[] = {6,1,2,3,4,4,5};
		InsertionSortReverse.sort(a);
		
		int b[] = {};
		InsertionSortReverse.sort(b);
		
		int c[] = {1};
		InsertionSortReverse.sort(c);
    }
}
