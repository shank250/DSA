
import TopicWiseQuestions.BitManipulaiton.*;
import java.util.ArrayList;
class RunnerFile{
    public static void main(String[] args) {
        Q78 solution = new Q78();
        // nums = [1,2,3]
        int[] nums = {1, 2, 3};
        ArrayList<ArrayList<Integer>> anser = solution.subsets(nums);
        System.out.println(anser);
    }
}