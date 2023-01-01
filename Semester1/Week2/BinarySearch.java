package Semester1.Week2;

public class BinarySearch {
    public Object search(int[] A, int target){
        int left = 1;
        int right = A.length;
        while(left <= right){
            int mid = left + (right - left) / 2;

            if(A[mid] == target){return mid;}
            else if(A[mid] < target){
                left = mid + 1;
            }else if (A[mid] > target){
                right = mid -1;
            }
        }

        return null;
    }
}
