import java.util.*;
class Solution {
    public boolean canJump(int[] nums) {
        /*
         * visiste each of the index and calculate the max possible distance we can travel
         *      if at some index max reach == current index and the element is 0
         */
        int maxReach = 0;
        for(int i = 0; i < nums.length; i++){
            maxReach = Math.max(maxReach, i + nums[i]);
            if(maxReach == nums.length - 1)
                return true;

            if(maxReach == i && nums[i] == 0)
                return false;
        }

        return true;
    }
}