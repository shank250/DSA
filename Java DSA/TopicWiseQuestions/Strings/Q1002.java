import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Q1002 {
    public static void main(String[] args) {
        String[] vals = {"hello", "mello"};
        List<String> ans = commonChars(vals);
        for (String val : ans) {
            System.out.println(val);
        }
    }

    public static List<String> commonChars(String[] words) {
        int target = words.length;
        HashMap<Character, Integer> hm = new HashMap<>();
        for (String word : words) {
            for (Character ch : word.toCharArray()) {
                hm.put(ch, hm.getOrDefault(ch, 0) + 1);
            }
        }
        List<String> rtn = new ArrayList<>();
        for (Character key : hm.keySet()) {
            if (hm.get(key) == target) {
                rtn.add(key + ""); // More efficient way to convert char to String: String.valueOf(key)
            }
        }
        return rtn;
    }
}
