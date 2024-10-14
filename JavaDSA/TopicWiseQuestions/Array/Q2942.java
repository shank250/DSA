import java.util.ArrayList;
import java.util.List;
class Q2942{
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> wordsContaining = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            // System.out.println(words.stringAt(i));
            for (int j = 0; j < words[i].length(); j++) {
                if (words[i].charAt(j) == x) {
                    wordsContaining.add(i);
                    break;
                }
            }
        }
        System.out.println(wordsContaining);
        return wordsContaining;
    }
}