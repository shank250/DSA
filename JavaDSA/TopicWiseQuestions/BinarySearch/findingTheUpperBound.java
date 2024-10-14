// package Java DSA.TopicWiseQuestions.BinarySearch;

public class findingTheUpperBound {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int x = Integer.parseInt(args[1]);
        int[] arr = new int[n];
        for(int i= 0 ; i < n; i++)
        {
            arr[i] = Integer.parseInt(args[2 + i]);
        }
        // question:
        // we have to find the ceiling of a number x in arr
        // this ceiling needs to be >= x but smallest in arr as much possible
        // if x is greater than grestest value of arr then return -1
        // solution:
        // we are by default taking a sorted arr
        // now intiate two pointers
        int low =0 , high = n-1, mid;
        int ans = -1;
        // how we will run a while loop with a condition that low<=high
        while(low <= high)
        {
            mid = (low + high)/2;
            if(x <= arr[mid])
            {
                ans = arr[mid];
                high = mid - 1;
            }
            else if(x > arr[mid])
            {
                low = mid + 1;
            }
        }
        System.out.println(ans);
    }
}
