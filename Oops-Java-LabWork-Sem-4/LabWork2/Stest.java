class Student {
    String name, city;
    int age;
    static int m; // static variable should be initialized outside of any method

    void printData() {
        System.out.println("Student name = " + name);
        System.out.println("Student city = " + city);
        System.out.println("Student age = " + age);
    }
}

public class Stest { // Corrected class declaration

    public static void main(String args[]) {
        Student s1 = new Student();
        Student s2 = new Student();
        s1.name = "Amit";
        s1.city = "Dehradun";
        s1.age = 22;
        s2.name = "Kapil";
        s2.city = "Delhi";
        s2.age = 23;
        s2.printData();
        s1.printData();
        s1.m = 20;
        s2.m = 22;
        Student.m = 27;
        System.out.println("s1.m = " + s1.m);
        System.out.println("s2.m = " + s2.m);
        System.out.println("Student.m =" + Student.m);
    }
}

