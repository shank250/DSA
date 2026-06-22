class Solution {
    public int minBitFlips(int start, int goal) {
        /*
         * Process each of the bits until the goal becomes zero.
         * Retrive each bits of start and goal and then make comparisons. 
         */
        if(start == goal) return 0;
        int ans = 0;

        while (goal != 0) {
            int a = start&1;
            int b = goal&1;

            if(a != b) ans++;
            
            goal = goal>>1
            start = start>>1;;
        }

        return ans;
    }
}