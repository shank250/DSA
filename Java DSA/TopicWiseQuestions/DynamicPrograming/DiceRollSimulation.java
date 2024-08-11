public class DiceRollSimulation {
    int[][] dp;
    private int find(int remN, int[] remRollMax){
        
        // base case: only when we reach the remN == 0
        if(remN == 0) return 1;

        int inter = 0;
        for(int i = 1; i < 7; i++){
            if(remRollMax[i - 1] != 0){
                remRollMax[i - 1] -= 1;
                if(dp[remN][i - 1])
                int val = + find(remN - 1, remRollMax);
                inter  = inter + val;
                remRollMax[i - 1] += 1;
            }
        }

        // for pair of remN and 

        return inter;
    }


    public int dieSimulator(int n, int[] rollMax) {
        dp = new int[n + 1][6];
        int ans = find(n, rollMax);        
        return ans;   
    }

    public static void main(String[] args) {
        DiceRollSimulation sol = new DiceRollSimulation();
        System.out.println(sol.dieSimulator(2, new int[]{1,1,1 , 1, 1, 1}));
    }
}
