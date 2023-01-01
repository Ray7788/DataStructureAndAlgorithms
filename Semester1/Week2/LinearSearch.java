package Semester1.Week2;

// O(n), average is O(n/2)
public class LinearSearch {
    public int search(int[] A, int q){
        int j = 1;
        while(j <= A.length && A[j] != q){
            j++;
        }

        if(j <= A.length){
            return j;
        }else{
            return -1;
        }
    }
}
