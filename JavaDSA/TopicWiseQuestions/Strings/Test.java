/**
 * Test
 */
public class Test {
    public static void main(String[] args) {
        String str1 = "   Hello World!   ";
        String str2 = "Java Programming";
        String str3 = "     ";

        System.out.println("Before trim: '" + str1 + "'");
        System.out.println("After trim: '" + str1.trim() + "'");

        System.out.println("Before trim: '" + str2 + "'");
        System.out.println("After trim: '" + str2.trim() + "'");

        System.out.println("Before trim: '" + str3 + "'");
        System.out.println("After trim: '" + str3.trim() + "'");
    }
}