import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Q119 
{
    private void  findRow(List<Integer> nums, int target)
    {
        if(nums.size() - 3 == target)
        {
            return;
        }
        for(int i = 0; i < nums.size() - 1; i++)
        {
            nums.set(i, (nums.get(i) + nums.get(i + 1)));
        }
        nums.add(0, 0);
        // nums.add(nums.size(), 0);
        findRow(nums, target);
    }
    public List<Integer> getRow(int rowIndex) 
    {
        List<Integer> nums = new ArrayList<Integer>();
        nums.addAll(Arrays.asList(0,1,0));
        if(rowIndex != 0)
        {
            findRow(nums, rowIndex);
        }
        return nums.subList(1, nums.size() - 1);
    }    
}
