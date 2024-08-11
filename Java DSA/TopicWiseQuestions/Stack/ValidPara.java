import java.io.*;
import java.util.Scanner;
import java.util.Stack;

/**
 * ValidPara
 */
public class ValidPara {

    private boolean validate(String str, Stack<Character> stack){
        boolean ans = true;
        int n = str.length();

        for(int i = 0; i < n; i++){
            char val = str.charAt(i);
            if (val == '(' || val == '{' || val == '[' ) stack.push(val);
            else{
                char other = stack.pop();
                if(val == '(' && other == ')' ||
                 val == '{' && other == '}' || 
                 val == '[' && other == ']') {
                    continue;
                 }else{;
                    return ans;
                 }
            }
        }
        return stack.size() == 0 ? true : false; 
    }


    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        String str = obj.nextLine();
        Stack<Character> stack = new Stack<>();
        ValidPara sol = new ValidPara();
        boolean ans = sol.validate(str, stack);
        System.out.println(ans);
    }

}