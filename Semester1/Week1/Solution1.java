public class Solution1 {
    public boolean search(int[] L, int k){
        for(int i = 0; i < L.length; i++){
            for(int j = i; j < L.length; j++){
                if (L[i] * L[j] == k){
                    return true;
                }
            }
        }

        return false;   
    }
}
