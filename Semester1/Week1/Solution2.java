import java.util.Arrays;

public class Solution2 {
    public boolean search(int[] L, int k){
        // 先排序
        Arrays.sort(L);

        int i = 0, j = L.length, value = 0; 

        while(i < j){
            value = L[i] * L[j];
            if(value == k){
                return true;
            }else if(value < k){
                i++;}
            else{
                j--;
            }
        }
        return false;
    }
}
