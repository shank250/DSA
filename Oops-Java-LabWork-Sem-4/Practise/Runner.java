import java.util.*;
class Runner
{
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < 4;i++)
        {
            list.add(i);
        }
        list.forEach(System.out::println);€
    }
}
