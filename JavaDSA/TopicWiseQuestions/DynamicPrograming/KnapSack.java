import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class KnapSack {
    public int greedyApproach(int n, int w, int[] weights, int[] price){

        PriorityQueue<Integer[]> maxHeap = new PriorityQueue<Integer[]>(
            // new Comparator<Integer[]>() {
            //     @Override
            //     public int compare(Integer[] a, Integer[] b) {
            //         return Integer.compare(a[0], b[0]);
            //     };
            // }
            // Comparator.reverseOrder()
        );

        for(int i = 0; i < n; i++){
            price[i] = price[i] / weights[i];
            maxHeap.add(new Integer[] {price[i], weights[i]});
        }

        Integer[] val;
        int profit = 0;
        while(w > 0){
            val = maxHeap.poll();
            for(int v: val){
                System.out.println(v);
            }
            if(w >= val[1]){
                profit += val[0]*val[1];
                w = w - val[1];
            }
            else{
                profit += val[0]*w;
                w = 0;
            }
        }

        return profit;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int w = scan.nextInt();
        int[] weights = new int[n + 1];
        int[] price = new int[n + 1];
        for(int i = 0; i < n; i++){
            weights[i] = scan.nextInt();
            price[i] = scan.nextInt();
        }
        scan.close();
        KnapSack sol =  new KnapSack();
        System.out.println("Greedy with Fractional part:" + sol.greedyApproach(n, w, weights, price));
    }
}
