public class Q330 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] vals = {2,4,56};
        System.out.println(sol.minPatches(vals, 7));
    }
    
}
class Solution 
{    
    public int minPatches(int[] nums, int n) 
    {    
        long check = 1; // checks if the number is in the array or not
        // and helps in deciding wheather to check next element or not
        int ptr = 0; // for nums
        int patchCnt = 0; // answer
        // we have to check and count the patches upto the n (inclusive)
        while(check <= n)
        {
            // check if the check is smaller than current element
            if(ptr >= nums.length || check < nums[ptr])
            {
                // if check is smaller then the current element of 
                // the array then it means that even the sum of all the
                // priveous elements of the array can not form the 
                // current element. Thus, in simple words we have to 
                // insert a new number into the array i.e. patchCnt++
                check += check; // here we are adding the nums[ptr]
                // beacuse now as this number is in the arrays so the sum 
                // will automaically contain this
                patchCnt++;
            }
            else
            {
                // so this is the case when the sum of all the visited array elements is more than the next element
                // which means that the next element can be easily formed by the available set of numbers in array
                // so we have to simply add that number into the check variable which means that we have to update our new visited array check sum
                check += nums[ptr];
                ptr++; // moving to the next element for checking
            }
        }
        return patchCnt;
    }
}