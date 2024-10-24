package JavaDSA.Algorithums;

/**
 * InsertionSort
 */
public class InsertionSort {

    private static void sort(int[] nums){
        int n = nums.length;
        
        if(n <= 1) return;

        for(int i = 1; i < n; i++){
            // we dont need to swap this much
            // we can shift all the elements by 1 unit that will be much better
            
            int j = i - 1;
            while(j >= 0){
                if(nums[j] > nums[j + 1]){
                    int temp = nums[j + 1];
                    nums[j + 1] = nums[j];
                    nums[j] = temp;
                    j--;
                }
                else break;
            }
        }

        return;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{2, 4, 1, 4, 3, 7, 4};
        sort(nums);
        for (int n : nums) {
            System.out.print(n + " ");
        }
    }
}