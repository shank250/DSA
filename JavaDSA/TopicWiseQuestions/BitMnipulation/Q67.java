/**
 * Q67
 */
public class Q67 
{
    private int stringToBinary(String binRep)
    {
        int ans = 0;
        int indx = 0;
        for(int i = binRep.length() - 1; i >=  0; i--)
        {
            char ch = binRep.charAt(i);
            if(ch == '1')
            {
                ans += Math.pow(2, indx); 
            }
            indx++;
        }
        return ans;
    }
    public String binaryToString(int num)
    {
        String ans = "";
        while(num != 1)
        {
            ans = ((num%2)) + ans;
            num = num / 2;
        }
        return ans;
    }
    public String addBinary(String a, String b)
    {
        int val1 = stringToBinary(a);
        int val2 = stringToBinary(b);
        val1 = val1 + val2;
        return binaryToString(val1);
    }
}