class MergeSort{
    private static void conqure(int[] nums, int left, int mid, int right){
        int[] merged = new int[right - left + 1];

        int ind1 = left, ind2 = mid + 1;
        int k = 0;

        while (ind1 <= mid && ind2 <= right) {
            if(nums[ind1] <= nums[ind2]){
                merged[k] = nums[ind1];
                ind1++;
            }else{
                merged[k] = nums[ind2];
                ind2++;
            }
            k++;
        }

        while(ind1 <= mid){
            merged[k] = nums[ind1];
            ind1++;
            k++;
        }


        while(ind2 <= right){
            merged[k] = nums[ind2];
            ind2++;
            k++;
        }

        for(int i = left, j = 0; i <= right;i++, j++){
            nums[i] = merged[j];
        }

        return;
    }

    private static void divide(int[] nums, int left, int right){
        if(left < right){

        
        int mid = left + (right - left)/2;

        divide(nums, left, mid);
        divide(nums, mid + 1, right);

        conqure(nums, left, mid, right);
        
        return;
    }
    }


    public static void sort(int[] nums){
        int n = nums.length;
        divide(nums, 0, n-1);
        return;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{
            1, 4,1, 5, 1, 5, 56,7, 2
        };

        sort(nums);

        for(int i:nums){
            System.out.print(i + " ");
        }
        System.out.println();
        return;
    }

}