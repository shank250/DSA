class Solution {
    public boolean checkValidString(String s) {
        /*
         * ---Inspired form others solution---
         * We can think of taking * as either ( / " "/ )
         * So, WE used 2 varibales which will cover different cases.
         * open_brack_min here if we get any * then we will assume that it is taken as )
         *      so, that we could try to coverup the parenthesis
         *      if open_brack_min < 0 then we can reset to 0 beacause then we are assuming * -> " "
         * other variable open_brack_max so here we will treat * as (
         *      so if somewhere this variable get open_brack_max < 0 means that the string is having more no of ((( bracks
         *      thus we will return false in this case 
         * 
         * after the whole traversal of the string if open_brack_min is positive no -> there are more opening brackets which cant be closed
         *      so return false
         * if open_bracket_min == 0 that means this could be a valid solution 
         *      return true
         */

        int open_brack_min = 0, open_brack_max = 0;
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(ch == '(') {open_brack_max++; open_brack_min++;} // these lines are like default cases
            else if(ch == ')') {open_brack_max--; open_brack_min--;}
            else {open_brack_max++; open_brack_min--;}
            
            if(open_brack_max < 0) return false;
            if(open_brack_min < 0) open_brack_min = 0;
        }

        return open_brack_min == 0 ? true : false;
    }
}