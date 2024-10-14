import java.util.Arrays;

/**
 * CombinationSumIV
 */
public class CombinationSumIV {
    int[] dp;
    private int find(int target, int[] nums, int[] dp){
        // call for each of the values of the nums
        // dp - key: 0 - target && target(if all the numbers are 1 then to create sum target we would require target no of memory)
        // base case: if the remaining sum becomes less than 0
        //  ONCE THINK ABOUT THE 0 INDEX
        if(target == 0) return 1;
        if(target < 0) return 0;
        if(dp[target] != -1) return dp[target];

        int sum = 0;
        for(int ele: nums){
            sum += find(target - ele, nums, dp);
        }

        dp[target] = sum;

        return sum;
    }

    public int combinationSum4(int[] nums, int target) {
        dp = new int[target + 1];
        // dp[0] : remaining target value
        // dp[1] : at which target level we are calculating
        Arrays.fill(dp, -1);
        int ans = find(target, nums, dp);
        return ans;
    }
    
    public static void main(String[] args) {
        CombinationSumIV sol = new CombinationSumIV() ;
        System.out.println(sol.combinationSum4(new int[] {1, 2, 3}, 4));
    }
}