import java.util.*;

class Solution {
    private int tryPossiblities(int l, int r, String s, int[][] map){
        if(l == r) return 1;
        if(l > r) return 0;
        if(map[l][r] != -1) return map[l][r];
        int interAns = 0;

        if(s.charAt(l) == s.charAt(r)){
            interAns = 2 + this.tryPossiblities(l + 1, r - 1, s, map);
        } 
        else{
            int a = this.tryPossiblities(l + 1, r, s, map);
            int b = this.tryPossiblities(l, r - 1, s, map);
            interAns = Math.max(a, b);
        }

        map[l][r] = interAns;
        return interAns;
    }

    public int longestPalindromeSubseq(String s) {
        /*
         * Take two pointers, one in front and another in the rear.
         * Then try out all the possible cases, if the pair of is valid the move to the inner string
         * else try to delete one character
         */
        int[][] map = new int[s.length() + 1][s.length() + 1];
        
        for(int i = 0; i < map.length; i++) 
            Arrays.fill(map[i], -1);

        return this.tryPossiblities(0, s.length() - 1, s, map);
    }
}