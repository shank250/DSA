import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
                // Create a new array to store Integer objects
        Integer[] peopleInteger = new Integer[people.length];

        // Populate the new array with Integer objects
        for (int i = 0; i < people.length; i++) {
          peopleInteger[i] = people[i];
        }

        // Sort the Integer array in descending order
        Arrays.sort(peopleInteger, Collections.reverseOrder());

        // (Optional) Copy elements back to an int array (if needed)
        for (int i = 0; i < people.length; i++) {
          people[i] = peopleInteger[i];
        }

        // Arrays.sort(people, Collections.reverseOrder());
        int boats = 0;
        int beg = 0;
        int end = people.length - 1;
        for (int num: people)
        {
            System.out.println(num);
        }
        while(beg <= end){
            int tmplimit = limit;
            tmplimit = tmplimit -  people[beg];
            if(tmplimit - people[end] >= 0)
            {
                --end;
            }
            ++beg;
            ++boats;
            System.out.println("init: "+ beg + " end: "+ end + " boats: " + boats);
        }

        return boats;
    }
}

class May$th{
    public static void main(String[] args){
        Solution obj = new Solution();
        int[] array = {3,2, 2,1};
        int ans = obj.numRescueBoats(array, 3);
        System.out.println(ans);
    }
}