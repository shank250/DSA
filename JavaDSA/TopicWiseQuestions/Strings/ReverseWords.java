import java.util.*;

class Solution {
    private StringBuilder appendBuilder(StringBuilder ans,String s,  int left, int right){
        while(left<=right)
            ans.append(s.charAt(left++));
        return ans;
    }
    public String reverseWords(String s) {
        /*Add " " this in front and end for processing, then start from the end of the String.
         * Take two pointers, one whicll move to the from until it get blank space, which will be updating with the right ptr.
         * Then once it found any char it would move ot the front of the string ans one another funciton will andd that whole word to the string (ans).
         */
        s = " " + s + " ";
        int left = s.length() - 2, right = left + 1;
        StringBuilder ans = new StringBuilder();
        while(left >= 0){
            if(s.charAt(left) == " "){
                right = left;
                left--;
            }
            else{
                while (s.charAt(left) != " ") left--;
                // call the function to add this left - right -> ans
                this.appendBuilder(ans, s, left, right);
                //updated the right
                right = left;
            }
        }
        ans.deleteCharAt(ans.length() - 1);
        return ans.toString();
    }
}