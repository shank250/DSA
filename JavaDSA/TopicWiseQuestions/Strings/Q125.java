
class Q125{
    public boolean isPalindrome(String s){
        s = s.toLowerCase();
        StringBuilder newS = new StringBuilder();

        for(int i = 0; i < s.length(); i++){
            int utfVal = s.charAt(i) - 'a';
            // if(s.charAt(i) =='9') System.out.println(utfVal);
            if((utfVal >= 0 && utfVal < 26) || (utfVal >= -49 && utfVal <= 40))
                newS.append(s.charAt(i));
        }
        System.out.println(newS);
        int left = 0, right = newS.length() - 1;
        while(left < right){
            if(newS.charAt(left) != newS.charAt(right))
                return false;
            left++;
            right--;
        }

        return true;
    }
    public static void main(String[] args) {
        Q125 obj = new Q125();
        System.out.println(obj.isPalindrome("p"));
    }
}