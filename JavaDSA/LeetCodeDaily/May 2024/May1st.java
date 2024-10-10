import java.util.*;

public class  May1st{
    public static void main( String args[]){
        Solution sol = new Solution();
        sol.reversePrefix("abcdefd", 'd');
        
    }
}
class Solution {
    public String reversePrefix(String word, char ch) {
        int index = -1;
        int noOfChar = word.length();
        for(int i = 0; i < noOfChar; i++){
            if (ch == word.charAt(i)){
                index = i + 1;
                break;
            }
        }
        System.out.println(index/2);
        for(int j = 0; j < index/2; j++){
            char tmp = word.charAt(j);
            char newChar = word.charAt(index - j - 1);
            word = word.substring(0, j) + newChar + word.substring(j+1, noOfChar);
            System.out.println(word);
            word = word.substring(0, index - j - 1) + tmp + word.substring((index - j - 1) + 1, noOfChar);
            System.out.println(word);
        }
        return word;
    }
}