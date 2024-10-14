import java.util.Scanner;

public class Q1922 {
    int limit = (int)1e9 + 7;
    private long power(long x, long y)
    {
        long temp; //  is this certain that we will return a int answer? -> no
        if(y == 1)
        {
            return x;// its a scenario where we have reached the base case for calculating the power
        }
        if(y == 0)
        {
            return 1;
        }
        temp = power(x, y/2);
        if(y%2 == 0)
        {
            return (temp*temp)%limit;
        }
        else
        {
            return (x*temp*temp)%limit;
        }
    }

    public int countGoodNumbers(long n)
    {
        // funtion implementation
        // here we have implement
        // 5^n/2 or 5^n/2+1 and 4^n/2
        // so to do that we may use normal pow function from the math package module 
        // but the problem is that it willl not give us correct andwer as the power can go upto 10^14
        // thus we will implement our own power function
        if(n%2 == 0)
        {
            return (int) (power(5, n/2)*power(4, n/2))%limit;
        }
        else
        {
            return (int) (power(5, n/2)*power(4, n/2 + 1))%limit;
        }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long val = scan.nextLong();
        Q1922 sol = new Q1922();
        int answer = sol.countGoodNumbers(val);
        System.out.println(answer);
    }
}
