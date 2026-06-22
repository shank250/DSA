import java.util.*;

class Solution {
    private int collide(int a, int b){
        if(Math.abs(a) == Math.abs(b)) return 0;
        return Math.abs(a) > Math.abs(b) ? a : b;
    }

    public int[] asteroidCollision(int[] asteroids) {
        /*
         * Start travelling the array
         *  if no is positive then simply add it into the stack
         *  else try to collide it with the top positive element of the stack
         *      if positive no is remaining then push it back into the stack 
         *      else again collide it with the positive no else push it into the stack
         * recompile each of them into an array in reverse order
         */
        Stack<Integer> stack = new Stack<>();
        int ptr = 0;
        
        while(ptr < asteroids.length){
            int astro = asteroids[ptr];
            if(astro > 0 || stack.size() == 0 || (astro < 0 && stack.peek() < 0)) 
                stack.push(asteroids[ptr++]);
            else
                if(stack.peek() > 0){
                    // collide both the astro and put the residual at the same ptr
                    // if nothing remains then move the ptr by 1
                    int resi = this.collide(astro, stack.pop());
                    if(resi != 0)
                         asteroids[ptr] = resi;
                    else{
                         ptr++;
                    }
                }
        }
        
        int[] ans = new int[stack.size()];
        for(int i = ans.length - 1; i >= 0; i--)
            ans[i] = stack.pop();
        
        return ans;
    }
}