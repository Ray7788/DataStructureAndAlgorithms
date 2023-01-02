package Semester1.Week3;

public class MergeSort {
    public void mergeSort(int[] src, int begin, int end){
		int mid = (end + begin)/2;

		if(begin < mid)	//1. 不要忘了这个条件，否则死递归退不出来。
			mergeSort(src, begin, mid);
		if(mid + 1 < end){	//同1
			mergeSort(src, mid + 1, end);
        }

		//  * 带“哨兵”的merge
		merge(src, begin, mid, end);
		
		//  * 练习题2.3-2不带哨兵的merge
		//new_merge(src, begin, mid, end);
	}


	//   带“哨兵”的原生态merge
	private void merge(int[] src, int begin, int mid, int end){
		if(src.length == 0 || src.length == 1)	//in case src is empty
			return;
		
		//初始化左右两个子数组，并且让数组末尾是“哨兵”
		int[] left = new int[mid - begin + 2];
		int[] right = new int[end - mid + 1];

		for(int i = 0; i < left.length - 1; i++){
			left[i] = src[begin + i];
		}

		left[left.length - 1]  = Integer.MAX_VALUE;		//2. 哨兵是个技巧，省略了每次判断是否左右数组越界的麻烦。
		
        for(int i = 0; i < right.length - 1; i++){
			right[i] = src[mid + i + 1];
		} 
        
		right[right.length - 1]  = Integer.MAX_VALUE;
		
		//开始merge
		int temp1 = 0;
		int temp2 = 0;
		for(int i = begin; i <= end; i ++){
			if(left[temp1] <= right[temp2])
				src[i] = left[temp1++];
			else
				src[i] = right[temp2++];
		}
	}



}
