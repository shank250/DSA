import java.util.Arrays;

public class Q238 {
    public static void main(String[] args) {
        int[] nums = {3, 2, 45, 2};
        int n = nums.length, forwProd = 1, backProd = 1, j;
        int[] ans = new int[n];
        Arrays.fill(ans, 1);
        for(int i = 1; i<n ; i++){
            j = n - i - 1;
            forwProd *= nums[i];
            backProd *= nums[j];
            ans[i] *= forwProd;
            ans[j] *= backProd;
        }
    }
}
