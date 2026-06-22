class Solution {
    public int jump(int[] nums) {
        /*
         * So, when i observed the constraints then i got one idea
         * That i can try to start the from the reae end and check how many steps will it take to 
         * reach the last index. 
         * in worst case we  have to check out 1000 indexs so thats all.
         * SO, i will keep an array which will keep the info of the no of steps 
         * and then come back to the starting index that how many steps are required which are min.
         */

        int[] memo =  new int[nums.length];
        if(nums.length == 1) return 0;

         for(int i = nums.length - 2; i >= 0; i--){
            int minPossi = Integer.MAX_VALUE;

            for(int j = 1; j <= nums[i] && (i + j < memo.length); j++){
                if(memo[i + j] != -1){
                    minPossi = Math.min(minPossi, memo[i + j]);
                }
            }

            if(minPossi == Integer.MAX_VALUE) memo[i] = -1;
            else memo[i] = 1 + minPossi;
         }
        
        return memo[0];
     }
}