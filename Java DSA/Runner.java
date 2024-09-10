
// import TopicWiseQuestions.BitManipulaiton.*;
// import java.util.ArrayList;
// class RunnerFile{
//     public static void main(String[] args) {
//         Q78 solution = new Q78();
//         // nums = [1,2,3]
//         int[] nums = {1, 2, 3};
//         ArrayList<ArrayList<Integer>> anser = solution.subsets(nums);
//         System.out.println(anser);
//     }
// }


// import java.util.Scanner;

// public class Runner {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         // Taking input for n (size of the array)
//         int n = scanner.nextInt();
        
//         // Creating an array of size n
//         int[] arr = new int[n];

//         // Taking input for the array elements
//         for (int i = 0; i < n; i++) {
//             arr[i] = scanner.nextInt();
//         }

//         // Taking input for k
//         int k = scanner.nextInt();

//         // Printing the inputs to verify
//         System.out.println("n: " + n);
//         System.out.print("arr: ");
//         for (int i = 0; i < n; i++) {
//             System.out.print(arr[i] + " ");
//         }
//         System.out.println();
//         System.out.println("k: " + k);

//         scanner.close();
//     }
// }
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Runner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();
        
        // Taking input for n (size of the array)
        int n = scanner.nextInt();
        scanner.nextLine();  // Consume the newline character after n

        // Taking input for the array elements in a single line
        int[] arr = new int[n];
        Arrays.fill(arr, 1);
        String[] input = scanner.nextLine().split(","); // Split the input line by spaces

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]); // Convert each part to an integer
        }

        // Taking input for k
        scanner.next();
        String k = scanner.nextLine();
    
        // Printing the inputs to verify
        System.out.println("n: " + n);
        System.out.print("arr: ");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        System.out.println("k: " + k);

        scanner.close();
    }
}
