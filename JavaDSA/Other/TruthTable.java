package Other;

import java.util.Scanner;

public class TruthTable {
    public void printTTRecursive(int[] nums, int index){
        if(index == nums.length){
            for (int i = 0; i < nums.length; i++)
                System.out.print(nums[i]);
            
            System.out.println();
            return;
            
        }
        nums[index] = 0;
        printTTRecursive(nums, index + 1);
        nums[index] = 1;
        printTTRecursive(nums, index + 1);
        return;
    }

    public void printTruthTable(int n){
        int[] nums = new int[n];
        printTTRecursive(nums, 0);
    }

    public static void main(String[] args) {
        TruthTable tt = new TruthTable();
        System.out.print("Enter the size of Truth Table: ");
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        scan.close();
        tt.printTruthTable(size);
        return;
    }
}
