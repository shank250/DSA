import java.util.ArrayList;
import java.util.*;


public class LoudandRich {
    /*
     * THis function is designed to return the indea of least quitest person who is 
     * richer than x.
     * and in the memory also the index are stored.
     */
   
     public static int findMinQuiteDfs(int x,List<List<Integer>> richer, int[] quiet, int[] memory){
        if(memory[x] != -1) return memory[x];
        int y = Integer.MAX_VALUE, inter;
        
        for(Integer xAdj : richer.get(x)){
            inter = findMinQuiteDfs(xAdj, richer, quiet, memory);
            if(y == Integer.MAX_VALUE) y = inter;
            if(quiet[y] > quiet[inter]) y = inter;
        }

        if(y == Integer.MAX_VALUE) y = x;
        memory[x] = y;

        return y;
    }
    
    public static int[] loudAndRich(int[][] richer, int[] quiet) {
        int[] quiteRicher = new int[quiet.length];
        Arrays.fill(quiteRicher, -1);
        List<List<Integer>> adjList = new ArrayList<>();
        for(int i: quiet){
            adjList.add(new ArrayList<>());
        }
        for(int[] ab : richer){
            adjList.get(ab[1]).add(ab[0]);
        }
        // int[] memory = new int[quiet.length]; 
        for(int i = 0; i < quiet.length; i++){
            quiteRicher[i] = findMinQuiteDfs(i, adjList, quiet, quiteRicher);
        }       
        return quiteRicher;
    }

    public static void main(String[] args) {
        
    }
}
