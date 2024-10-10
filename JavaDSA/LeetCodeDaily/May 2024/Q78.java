import java.util.ArrayList;
class Q78
{
    public ArrayList<ArrayList<Integer>> subsets(int[] nums)
    {
        // CREATE A 2D LIST
        ArrayList<ArrayList<Integer>> rtn = new ArrayList<ArrayList<Integer>>();
        rtn.add(new ArrayList<Integer>());
        System.out.println(rtn);

        // SELECT ONE BY ONE EACH ELEMENT OF THE NUMS
        for(int num:nums)
        {
            // THEN TAKE EACH ELEMENT OF THE 2D LIST AND APPEND THE NEW NUM AND ADD THAT LIST TO THE 2D LIST
            for(ArrayList<Integer> list : rtn)
            {
                ArrayList<Integer> newList = new ArrayList<Integer>();
                newList.addAll(list);
                newList.add(num);
                rtn.add(newList);
            }
        }
        // RETURN THE LIST
        return rtn;
    }
}