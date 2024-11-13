package Other;

import java.net.Socket;

public class BinaryArray {
    public static void sumArray(int[] nums){
        int n = nums.length, i = 0, prev = 0;
        
        while (i < n) {

            if(nums[i] == 0){
                if(prev != 0)
                    System.out.print(prev + " ");
                
                System.out.print(nums[i] + " ");
                prev = 0;;
            }

            prev++;
            i++;
        }
        if(prev != 0)
            System.out.println(prev);
    }
    public static void main(String[] args) {
        int[] nums = new int[]{ 0, 1,  1};
        sumArray(nums);

    }
}
