import java.util.Arrays;
import java.util.HashMap;

public class PartitionEqualSubset {
// boolean[] dp;
    HashMap<Integer, Boolean> dp;
    private boolean find(int index, int target, int[] nums, int presum){
        boolean pick, dontpick;
        if(presum == target){
            System.out.println("test 2");
            return true;
        }
        if(dp.containsKey(presum)) return dp.get(presum);
        // if(dp[presum] != null) return dp[presum]; 

        if(index == nums.length || presum > target){ 
            // dp[presum] = false;
            return false;
            }

        pick = find(index + 1, target, nums, presum + nums[index]);
        dontpick = find(index + 1, target, nums, presum);

        // dp[presum] = pick | dontpick;
        dp.put(presum, pick || dontpick); 
        return pick || dontpick;
    }


    public boolean canPartition(int[] nums) {
        int sum = 0, target;
        for(int num: nums) sum += num;
        if(sum % 2 == 0) target = sum / 2;
        else return false;
        System.out.println("test 1");
        dp = new HashMap<>();
        // dp = new boolean[target + 1];
        // System.out.print(dp[1]);
        return find(0, target, nums, 0);
    }
    public static void main(String[] args) {
        PartitionEqualSubset sol = new PartitionEqualSubset();
        int[] nums = new int[] {18,17,18,11,15,4,13,11,9};
        Arrays.sort(nums);
        boolean ans = sol.canPartition(nums);
        System.out.println(ans);
    }
}
