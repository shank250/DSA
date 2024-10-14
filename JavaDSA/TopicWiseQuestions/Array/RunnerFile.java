// import java.utils.String;

class RunnerFile{
    public static void main(String[] args) {
        Q1672 solution = new Q1672();
        // String myString = new String();
        // String myString = "leet code";
        // String[] listString = myString.split(" ");
        // System.out.println(listString);
        int[][] newList = {{1,2,3},{3,2,1}};
        int ans = solution.maximumWealth(newList);
        System.out.println(ans);
    }
}