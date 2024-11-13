package TopicWiseQuestions.Array;

public class Q2149 {
    public int[] rearrangeArray(int[] nums) {
        /*This method initially filters the positives and negatives
         * Then we put positive and negative alternativily.
         */
        int[] positiveNo = new int[nums.length/2];
        int[] negativeNo = new int[nums.length/2];
        int pInd = 0, nInd = 0;
        
        for(int num: nums){
            if(num >= 0) positiveNo[pInd++] = num;
            else negativeNo[nInd++] = num;
        }
            
        for(int i = 0; i < nums.length / 2; i++){
            nums[i*2] = positiveNo[i];
            nums[i*2 + 1] = negativeNo[i];
        }

        return nums;
    }
}