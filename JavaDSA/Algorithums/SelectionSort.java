package JavaDSA.Algorithums;

public class SelectionSort {
    private static void sort(int[] nums){
        int n = nums.length;

        for(int i = 0; i < n; i++){
            int indexMaxValue = i;
            
            for(int j = i; j < n; j++){

                if(nums[j] > nums[indexMaxValue]){
                    indexMaxValue = j;
                }

            }

            int temp = nums[i];
            nums[i] = nums[indexMaxValue];
            nums[indexMaxValue] = temp;
        }

        return;
    } 

    public static void main(String args[]){
        int[] nums = new int[]{3, 2, 1, 5, 7, 2};

        sort(nums);

        for (int n : nums) {
            System.out.println(n);
        }

        return;
    }
}
