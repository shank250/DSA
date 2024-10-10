import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class CombinationSum {
   
    Set<HashMap<Integer, Integer>> set;
    int size = 0;
    private void subsets(HashMap<Integer, Integer> hm, int[] candidates, int prevSum, int target){

        for(int i = 0; i < size; i++){
            hm.put(i, hm.getOrDefault(i, 0) + 1);
            if(prevSum + candidates[i] == target){
                set.add(hm);
            }
            if(prevSum + candidates[i] > target){
                hm.put(i, hm.getOrDefault(i, 0) - 1);
                return;
            }
            subsets(hm, candidates, prevSum + candidates[i], target);
            hm.put(i, hm.getOrDefault(i, 0) - 1);
        }

    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        set = new HashSet<>();
        size = candidates.length;
        Arrays.sort(candidates);
        for(int i = 0; i< size;i++){
            hm.put(i, 0);
        }
        subsets(hm, candidates, 0, target);
        List<List<Integer>> mylist = new ArrayList<>();
        System.out.println(set);
        for(HashMap<Integer, Integer> ihm : set){
            List<Integer> sublist = new ArrayList<>();
            for(int key: ihm.keySet()){
                for(int i = 0; i < ihm.get(key); i++){
                    sublist.add(candidates[i]);
                }
                mylist.add(sublist);
            }
        }
        return mylist;

    }
    public static void main(String[] args) {
        CombinationSum sol = new CombinationSum();
        List<List< Integer>> ans = sol.combinationSum(new int[] {2 , 3, 5}, 8);
        System.out.println(ans);
    }
}
