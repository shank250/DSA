/**
 * Q1051
 */
// import java.util.*;
public class Q1051 {
    public static void main(String[] args) {
        int[] heights = {1,1,4,2,1,3};
        int[] sorted = heights.clone();
        int temp;
        for(int i = 0; i < heights.length - 1; i++)
        {
            for(int j = 0; j < heights.length - 1 - i; j++)
            {
                if(sorted[j] > sorted[j+1])
                {
                    temp = sorted[j + 1];
                    sorted[j + 1] = sorted[j];
                    sorted[j] = temp;
                }
            }
        }
        for(int val:sorted)
        {
            System.out.print(val + " ");
        }
    }
}