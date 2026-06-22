import java.util.*;

class Solution {
    private int sumDivisions(int[] nums, int div){
        _sum = 0;
        for(int n: nums){
            _sum += Math.ceilDiv(n, div);
        }
        return _sum;
    }
    public int smallestDivisor(int[] nums, int threshold) {
        /* So, the approach is to start searching for the correct positive integer,
         * but here i will be using binary search for this searching.
         * On analysis low = 1, and high = max(nums)
         * then if the sum(nums/mid) > th then low -> mid  + 1
         * else if sum(nums/mid) <= th then  high -> mid - 1 (this could be one of the sol)
         */
        // Arrays.sort(nums);
        int low = 1, high = 0;
        for(int n: nums)
            high = Math.max(high, n);
        int possiSol = high;
        
        while(low <= high){
            mid = low + (high - low)/2;
            int _sum = sumDivisions(nums, mid);
            
            if(_sum > threshold) low = mid + 1;
            else{
                possiSol = Math.min(mid, possiSol);
                high = mid - 1;
            }
        }

        return possiSol;
    }
}