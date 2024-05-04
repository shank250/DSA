import java.util.ArrayList;


class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1array = version1.split("[.]");
        String[] v2array = version2.split("[.]");
        int v1len = v1array.length;
        int v2len = v2array.length;
        int index = 0;
        int comp1, comp2;
        while(index != Math.max(v1len, v2len)){
            if (index >= v1len)
            {
                comp1 = 0;
            }
            else{
                comp1 = Integer.parseInt(v1array[index]);
            }
            if (index >= v2len)
            {
                comp2 = 0;
            }
            else{
                comp2 = Integer.parseInt(v2array[index]);
            }
            if (comp1 > comp2){
                return 1;
            }
            else if(comp1 < comp2){
                return -1;
            }
            else{
                index++;
            }
        }
        return 0;
    }
}

class May3rd{
    public static void main(String[] args){
        Solution obj = new Solution();
        int ans = obj.compareVersion("1.01", "1.001.0");
        System.out.println(ans);
    }
}