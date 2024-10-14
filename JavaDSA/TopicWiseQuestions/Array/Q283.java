class Q283
{
    public void moveZeroes(int[] nums) 
    {
        int zeorsCount = 0, length = nums.length;
        for(int i = 0; i < length; i++)
        {
            if(nums[i] == 0)
            {
                zeorsCount++;
            }
            else
            {
                nums[i - zeorsCount] = nums[i];
            }
        }
        while (zeorsCount > 0) {
            nums[length - zeorsCount] = 0;
            zeorsCount--;
        }
        for(int n: nums)
        {
            System.out.println(n);
        }
    }
    public static void main(String[] args) {
        Q283 shiftZeroes = new Q283();
        int[] nums = {0,1,0,3,12};
        shiftZeroes.moveZeroes(nums);
    }
}