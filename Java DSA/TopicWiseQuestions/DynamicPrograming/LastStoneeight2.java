import java.util.HashMap;

/**
 * LastStoneeight2
 */
public class LastStoneeight2 {
    HashMap<String, Integer> dHashMap = new HashMap<>();
    private int collision(int[] stones, int index, int total, int totalSum) {
        if(((int) totalSum / 2 ) + 1  <=  total || index == stones.length) 
            return Math.abs(totalSum - (2*total));

        if(dHashMap.containsKey((String) "" + index + "," + total)) return dHashMap.get((String) "" + index + "," + total);

        int residualstone = Math.min(collision(stones,  index + 1, total, totalSum),
                                    collision(stones, index + 1, total + stones[index], totalSum));
        
        dHashMap.put((String) "" + index + "," + total, residualstone);
        
        System.out.println("At index: " + index + " residualStone: " + residualstone + " index: " + stones.length);
        return residualstone;
    }

    public int lastStoneWeightII(int[] stones) {
        // i need to MAKE make two subarrays
        // and thees subarrays sub should be very close to the total subarray sum by 2
        int totalSum = 0;
        for (int st : stones) totalSum += st;
        //Adding dp in the above question

        // now i need to calculate all the possible sums of subarrays which are less than
        // totalSum / 2. So lets use recursion to form this
        return collision(stones, 0, 0, totalSum);        
    }

    public static void main(String[] args) {
        // we are give a stones array
        // we need to find minimum residual stone after collisions
        int[] stones = {89,23,100,93,82,98,91,85,33,95,72,98,63,46,17,91,92,72,77,79,99,96,55,72,24,98,79,93,88,92};
        LastStoneeight2 obj = new LastStoneeight2();
        int ans = obj.lastStoneWeightII(stones);
        System.out.println(ans);
    }
}