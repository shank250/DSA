import java.util.Arrays;

public class PerfecctSquare {

    private int find(int n, int[] dp){
        // returning the answer if we have previosuly calculated
        if(dp[n] != -1) return dp[n];

        // this will help in finding all the other possible integers whose sq could make the sum equals to n
        int sqrt = (int) Math.sqrt(n); 
        int minStep = 10001; // mini steps required to form this n 

        // termianation condition
        if(n == 0) return 0;

        for(int i = sqrt; i > 0; i--){
            // again calling the same function but with the 
            // remaining number after subtracting i^2 from my n
            int remaining = n - i*i;
            minStep = Math.min(minStep, 1 + (find(remaining, dp)));
        }

        dp[n] = minStep;
        return minStep;
    }

    public int numSquares(int n) {
        // we can also initialise n+1 dp and dp[0] = 0 
        // in that case we can remove the 0 returning statement from find() method
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        return find(n, dp);
    }
    

    public static void main(String[] args) {
        PerfecctSquare obj = new PerfecctSquare();
        System.out.println(obj.numSquares(13));
    }
}
