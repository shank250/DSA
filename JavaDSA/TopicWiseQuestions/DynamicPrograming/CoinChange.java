class CoinChange 
{
    public int coinChange(int[] coins, int amount) 
    {
        int n = coins.length;
        int[] dp = new int[++n];
        dp[0] = 0;

        for(int i = 1; i < n; i++)
        {
            dp[i] = Integer.MAX_VALUE;
            for(int coin: coins)
            {   
                if(i - coin < 0) break;
                // if we can take this coin or not
                if(dp[i - coin] != Integer.MAX_VALUE ) dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
            }
        }
        return dp[n-1] == Integer.MAX_VALUE ? -1 : dp[n - 1];
    }
}