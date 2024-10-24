import java.util.PriorityQueue;
import java.util.Collections;

public class MinTotalWeight {
    
    public static int minTotalWeight(int[] chocolates, int d) {
        // Create a max-heap using a priority queue with reverse order (to behave like max-heap)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        // Add all chocolate weights to the max-heap
        for (int choc : chocolates) {
            maxHeap.add(choc);
        }
        
        // Perform d iterations to minimize the total weight
        for (int i = 0; i < d; i++) {
            // Extract the heaviest chocolate
            int heaviest = maxHeap.poll();
            
            // Eat half of the chocolate
            int eaten = heaviest / 2;
            int remaining = heaviest - eaten;
            
            // Push the remaining half back into the heap
            maxHeap.add(remaining);
        }
        
        // Calculate the total remaining weight
        int totalRemainingWeight = 0;
        while (!maxHeap.isEmpty()) {
            totalRemainingWeight += maxHeap.poll();
        }
        
        return totalRemainingWeight;
    }

    public static void main(String[] args) {
        int[] chocolates = {20, 25, 30};
        int d = 4;
        System.out.println(minTotalWeight(chocolates, d));  // Example usage
    }
}
