package JavaDSA.Algorithums;

public class BubbleSort {
    private static void sort(int[] arr){
        int n = arr.length;

        for(int i = 0; i < n - 1; i++){
            boolean swapOccured = false;

            for(int j = 0; j < n - i - 1; j++){
            
                if(arr[j + 1] < arr[j]){
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                    swapOccured = true;
                }
            
            }
            // this check can decrease the time complexity in some cases
            
            if(!swapOccured)
                return;
        
        }

        return;
    } 

    public static void main(String[] args){
        int[] nums = new int[]{2, 3, 1, 5, 6, 2, 7, 4};
        sort(nums);
        for (int i : nums) {
            System.out.print(i + " ");
        }
    }
}
