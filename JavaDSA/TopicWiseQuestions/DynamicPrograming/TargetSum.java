import java.util.Arrays;

public class TargetSum {
    int[][] dp;
    int sum = 0;
    private int find(int[] nums, int target, int index, int eval){
        // base case: when index is out of bound the list length
        // otherwise calculate eval
        if(index == nums.length) return eval == target ? 1 : 0;

        // dp : eval + sum :: indexing for the dp matrix[-][]
        //      index :: indexing for the dp matrix[][-]
        
        if(dp[eval + sum][index] != -1) return dp[eval + sum][index];

        int val = find(nums, target, index + 1, eval + nums[index]) +  find(nums, target, index + 1, eval - nums[index]);
        
        dp[eval + sum][index] = val;
        return val;
    }

    public int findTargetSumWays(int[] nums, int target) {
        for(int val: nums) sum += val;
        dp = new int[(sum)*2 + 1][nums.length + 1];
        for(int i = 0; i < dp.length; i ++ ){
            Arrays.fill(dp[i], -1);
        }
        int ans = find(nums, target, 0, 0);
        return ans;
    }

    public static void main(String[] args) {
        TargetSum obj =  new TargetSum();
        System.out.println(obj.findTargetSumWays(new int[]{1,1,1,1,1}, 3));
    }
}
