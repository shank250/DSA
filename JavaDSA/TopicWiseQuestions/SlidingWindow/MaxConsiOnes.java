import java.util.*;

class Solution {
    public int longestOnes(int[] nums, int k) {
        /*
         * Here I am trying to create the max possible size of the window with 
         * the given no of conversions
         */
        int l = 0;
        
        for(int r = 0; r < nums.length; r++){
            k -= 1 - nums[r];

            if(k < 0){
                if(nums[l] == 0) k++;
                l++;
            }
        }        
        
        return r - l + 1;
    }
}