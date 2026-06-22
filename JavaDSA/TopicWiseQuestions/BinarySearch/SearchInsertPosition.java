class Solution {
    public int searchInsert(int[] nums, int target) {
        /*
         * implement simple binary search
         * then we need to handle the case when we do not find the value and need to return the value.
         */

        int low = 0, high = nums.length - 1, mid;
        
        while(low <= high){
            mid = low + (high - low)/2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                low = mid + 1;
            else
                high = low - 1;

            System.out.println("low: " + low + " mid: " + mid + " high: " + high);
        }

        return low;
    }
}