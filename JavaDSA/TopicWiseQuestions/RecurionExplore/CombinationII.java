import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;

class Solution {
    private void travel(int index, int n, int[] candidates, int target, List<List<Integer>> ans, List<Integer> curArr,  int[][] memo){
        if(target == 0){
            // possible solution
            ans.add(new ArrayList<>(curArr));
            return;
        }
        if(index == n || target < 0 || memo[target][index] == 1) return;
        
        //dont pick
        this.travel(index + 1, n, candidates, target, ans, curArr, memo);

        //pick
        curArr.add(candidates[index]);
        this.travel(index + 1, n, candidates, target - candidates[index], ans, curArr, memo);
        curArr.remove(curArr.size() - 1);

        memo[target][index] = 1;

        return;
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        /*
         * just doing noraml pick and not pick approach
         */
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> posAns = new ArrayList<>();
        int[][] memo = new int[target + 1][candidates.length + 1];
        Arrays.sort(candidates);
        
        this.travel(0, candidates.length, candidates, target, ans, posAns, memo);

        return ans;
    }
}