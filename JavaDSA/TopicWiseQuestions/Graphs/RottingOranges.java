import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        /* 
        Initially count the no of rotten oranges and total no of oranges
        Then push the rotten oranges into the queue
        Now process the queue by visiting all the neighbours of the rotten orange
            and put them into the queue.
        Continue this untill the queue is empty
            if the no of new rotten and odl rotten equals total no of oranges then return the time it took 
            else return -1
        */
        Queue<int[]> queue = new LinkedList<>();
        int oldRotten = 0, totalOranges = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 2){
                    queue.offer(new {i, j});
                    oldRotten++;
                }
                if(grid[i][j] == 1 || grid[i][j] == 2) totalOranges++;
            }
        }
        int newRotten = 0, noOfMin = 0;
        while(!queue.isempty()){
            int size = queue.size();
            int[] dx = new {1, -1, 0, 0};
            int[] dy = new {0, 0, 1, -1};

            for(int i = 0; i < size; i++){
                int[] cord = queue.poll();
                int x = cord[0];
                int y = cord[1];
                for(int j = 0; j < 4; j++){
                    if(x + dx[j] < grid.length && y + dy[j] < grid[0].length && x + dx[j] >= 0 && y + dy[j] >= 0 && grid[x + dx[j]][y + dy[j]] == 1){
                        grid[x + dx[j]][y + dy[j]] = 2;
                        queue.offer(new {x + dx[j], y + dy[j]});
                        newRotten++;
                    }
                }
            }
            noOfMin++;
        }
        if(newRotten + oldRotten == totalOranges) return noOfMin;
        return -1;
    }
}