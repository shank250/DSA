import java.util.ArrayList;

class May20th{
    public int subsetSum(Integer integer, int xorSubsetValue){
        int sum = 0;
        for (int i = 0; i < integer.size(); i++){
            sum += subsetSum(integer.remove(i), xorSubsetValue^(integer.get(i)));
        }
        return sum;
    }
    public static void main(String[] args){
        int[] nums1 = {1,3};
        int xorVal = 0;
        ArrayList<Integer> nums = new ArrayList<>();
        for(int i = 0; i < nums1.length; i++){
            nums.add(nums1[i]);
            xorVal ^= nums1[i];
        }
        May20th myobj = new May20th();

        int answer = myobj.subsetSum(nums, xorVal);
        System.out.println(answer);
    }
}