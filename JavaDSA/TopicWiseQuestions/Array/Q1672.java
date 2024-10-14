class Q1672{
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0; 
        int noOfCust = accounts.length;
        for(int i = 0; i < noOfCust;i++ ){
            int noOfAccount = accounts[i].length;
            int custSum = 0;
            for(int j = 0; j < noOfAccount; j++)
            {
                custSum += accounts[i][j];
            }
            if(custSum>maxWealth)
            {
                maxWealth = custSum;
            }
        }
        return maxWealth;
    }
}