package JavaDSA.Algorithums;

public class QuickSort {
    private static int partition(int[] nums, int left, int right){
        int i = left - 1;
        int pivot = nums[right];

        for(int j = left; j < right; j++){
            if(nums[j] < pivot){
                i++;
                // swap
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }

        i++;
        nums[right] = nums[i];
        nums[i] = pivot;

        return i;
    } 


    private static void sort(int[] nums, int left, int right){
        if(left >= right)
            return;
 
        int indPivot = partition(nums, left, right);

        sort(nums, left, indPivot - 1);
        sort(nums, indPivot + 1, right);

    } 
}
