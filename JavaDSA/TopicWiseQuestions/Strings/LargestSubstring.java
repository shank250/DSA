import java.util.Scanner;

public class LargestSubstring {

    public boolean checkPalindrom(String s, int size){
        int start = 0, end = size - 1;
        while(start < size){
            if(s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
    
    
    public String longestPalindrome(String s) {
        
        for(int size = s.length(); size >= 0 ; size--){
            for(int init = 0; init + size <= s.length(); init++){
                if(checkPalindrom(s.substring(init, init + size), size) == true) 
                    return s.substring(init, init + size);
            }
        }

        return s;
    }

    public static void main(String[] arg){
        String s = "cbbd";
        
        LargestSubstring sol = new LargestSubstring();
        String ans = sol.longestPalindrome(s);
        System.out.println(ans);

    }
}
