class BinarySearch{
    private static int search(int[] nums, int k){
        int left = 0 , right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left)/2;

            if(nums[mid] == k){
                return mid;
            }

            if(nums[mid] < k){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }

        }

        return -1;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 4, 6, 7, 44, 77, 88};
        int k = 7;
        
        
        int asn = search(nums, k);
        System.out.println(asn);
        return;
    }
}