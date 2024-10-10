import java.util.Arrays;

public class KnightDialer {
    int[][] dp;
    private int find(int currentKey, int remainingSteps){
        // writing the code for each of the keys where knight possibly reach
        int val = 0;
        // System.out.println(remainingSteps);
        if(remainingSteps <= 0) return 1;
        if(dp[remainingSteps][currentKey] != -1) return dp[remainingSteps][currentKey];
        if(currentKey == 1){
            val = (val + find(6, remainingSteps-1))%(1_000_000_007);
            val = (val + find(8, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 2){
            val = (val + find(7, remainingSteps-1))%(1_000_000_007);
            val = (val + find(9, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 3){
            val = (val + find(4, remainingSteps-1))%(1_000_000_007);
            val = (val + find(8, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 4){
            val = (val + find(3, remainingSteps-1))%(1_000_000_007);
            val = (val + find(9, remainingSteps-1))%(1_000_000_007);
            val = (val + find(0, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 5) return 0;
        else if(currentKey == 6){
            val = (val + find(1, remainingSteps-1))%(1_000_000_007);
            val = (val + find(7, remainingSteps-1))%(1_000_000_007);
            val = (val + find(0, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 7){
            val = (val + find(2, remainingSteps-1))%(1_000_000_007);
            val = (val + find(6, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 8){
            val = (val + find(1, remainingSteps-1))%(1_000_000_007);
            val = (val + find(3, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 9){
            val = (val + find(2, remainingSteps-1))%(1_000_000_007);
            val = (val + find(4, remainingSteps-1))%(1_000_000_007);
        }else if(currentKey == 0){
            val = (val  + find(4, remainingSteps-1))%(1_000_000_007);
            val = (val + find(6, remainingSteps-1))%(1_000_000_007);
        }
        val = val%(1_000_000_007);
        dp[remainingSteps][currentKey] = val;
        return val;
    }


    public int knightDialer(int n) 
    {
        if(n == 0) return 0;
        dp = new int[n + 1][10];
        for(int j  = 0; j < n + 1; j++){
            Arrays.fill(dp[j], -1);    
        }
        // for(int[] list: dp){
        //     for(int ele: list) System.out.print(ele + " ");
        //     System.out.println();
        // }
        int ans = 0;
        for(int i = 0; i<= 9; i++){
           ans = (ans + find(i, n - 1))%(1_000_000_007);
        }
      
       
        return ans%(1_000_000_007);
    }
    public static void main(String[] args) {
        KnightDialer sol = new KnightDialer();
        int answer = sol.knightDialer(3131);
        System.out.println(answer);
    }
}
