import java.util.Arrays;

public class Q6 {
    private static int travelBottom(int x, int y, char[][] matrix, int ptr, String s, int numRows){
        int n = s.length();
        if(ptr == n) return x;

        while(y < numRows){
            if(ptr == n) return x;
            
            matrix[y][x] = s.charAt(ptr);
            ptr++;
            
            y++;
        }

        return travelDiagonal(x + 1, y - 2, matrix, ptr, s, numRows);
    }

    private static int travelDiagonal(int x, int y, char[][] matrix, int ptr, String s, int numRows){
        // terminaltion condition - if no string is remaining to process
        int n = s.length();
        if(ptr == n) return x;

        while(y >= 0){
            if(ptr == n) return x;
            
            matrix[y][x] = s.charAt(ptr);
            x++;
            ptr++;
            
            y--;
        }

        return travelBottom(x - 1, y + 2, matrix, ptr, s, numRows);
    }


    public String convert(String s, int numRows) {
        char[][] matrix = new char[numRows][s.length()];
        StringBuilder str = new StringBuilder();
        
        if(numRows == 1) return s;
        for(int i = 0; i < numRows; i++) Arrays.fill(matrix[i], '-');
        
        int x = Q6.travelBottom(0, 0, matrix, 0, s, numRows);

        for(int i = 0; i < numRows; i++)
            for(int j = 0; j < x + 1; j++)
                if(matrix[i][j] != '-') str.append(matrix[i][j]);

        return str.toString();
    }


    public static void main(String[] args) {
        Q6 obj = new Q6();
        String ans = obj.convert("paypalishiring", 4);
        System.out.println(ans);
        return;
    }
}
