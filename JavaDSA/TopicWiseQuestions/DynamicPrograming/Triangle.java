import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Triangle {
    // HashMap<String, Integer> dHashMap = new HashMap<>();
    Integer[][] dp;    
    private int findMin(int i, int j, List<List<Integer>> triangle, Integer[][] dp){
        // termination condition - base case
        if(triangle.size() == j + 1) return triangle.get(j).get(i);

        // if(dHashMap.containsKey("" + i + "," + j)) return dHashMap.get("" + i + "," + j);
        if(dp[j][i] != null) return dp[j][i];
        // recursive calls
        int minSum = triangle.get(j).get(i) + Math.min(findMin(i, j + 1, triangle, dp), 
                            findMin(i + 1, j + 1, triangle, dp));

        // dHashMap.put("" + i + "," + j, minSum);
        dp[j][i] = minSum;
        return minSum;
    }

     public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        dp = new Integer[n +1][n + 1];
        return findMin(0, 0, triangle, dp);
    }

    public static void main(String[] args) {
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();

        
    
    }   
}
