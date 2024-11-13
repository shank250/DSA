class QuickSort{
    // finding the pivot point in a given array
    private static int findPivot(int[] nums, int left, int right){
        int i = left - 1;
        int pivot = nums[right];

        for(int j = left; j < right; j++){
            if(nums[j] <= pivot){
                i++;
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
            }
        }

        i++;
        int tmp = nums[right];
        nums[right] = nums[i];
        nums[i] = tmp;

        return i;
    }


    // function calling which partitions the array in two parts from the pivot
    private static void makePartition(int[] nums, int left, int right){
        if(left >= right)
            return;

        int indpivot = findPivot(nums, left, right);

        makePartition(nums, left, indpivot - 1);
        makePartition(nums, indpivot + 1, right);

        return;
    }

    public static void sort(int[] nums){
        int n = nums.length;
        makePartition(nums, 0, n - 1);
    }


    public static void main(String[] args) {
        int[] nums = new int[]{3, 5,6 ,2 ,6, 2, 5,78};

        sort(nums);
        
        for (int i : nums) {
            System.out.print( i + " ");
        }
    }
}