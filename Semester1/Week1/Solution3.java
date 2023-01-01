import java.util.HashSet;

public class Solution3 {
    // Let S be an empty set
    HashSet<Integer> S= new HashSet<>();
    
    public boolean search(int[] L, int k){
        for (int i = 0; i <L.length; i++){
            int a = L[i];

            // if a divides k then
            if (k % a == 0){
                S.add(a);
            }

            int b = k / a;
            if(S.contains(b)){
                return true;
            }
        }
        
        return false; 
    }
}
