package TopicWiseQuestions.Strings;

public class Q680 {
    private boolean checkValid(String s, int left, int right, boolean oneEleDeleted){
        /*Function to check the left and right characters and converge until
         * different characters occurs.
         * If different characters have occured then we have to check either one element has been 
         * already deleted or not. If yes then we cant delete one more charater, thus return false.
         * Else we will delete/skip one charater from left and one character from right, and again
         * recursivily calling the same function.
         */

        while(left < right){
            if(s.charAt(left) == s.charAt(right)){
                left++;
                right--;
            }
            else{
                if(oneEleDeleted) return false;
                return checkValid(s, left + 1, right, true) ||
                        checkValid(s, left, right - 1, true);
            }
        }

        return true;
    }

    public boolean validPalindrome(String s) {
        return checkValid(s, 0, s.length() - 1, false);
    }
}
