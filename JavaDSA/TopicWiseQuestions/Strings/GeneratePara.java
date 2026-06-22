import java.util.*;

class Solution {
    private void addPara(int left, int right,  Set<String> ans, String para, int size, int n){
        if(size == n*2){
            ans.add(para);
            return;
        }

        if(left < n)
            addPara(left + 1, right, ans, "(" + para, size, n);

        if(right < n)
            addPara(left, right + 1, ans, para + ")", size, n);
        
        return;
    }
    public List<String> generateParenthesis(int n) {
        /* Just used simple recursion to find all the possible combinations of the para.
        Used set to remove duplicates. */
        List<String> ans = new ArrayList<>();
        
        addPara(left, right,  ans, "", size, n);
        
        return new ArrayList<String>(ans);
    }
}