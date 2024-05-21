/**
 * main
 */
class New {

    public static void main(String[] args) {
        User user1 = new User();
        user1.setAge(4);
        user1.setName("Me");
        System.out.println(user1.getAge());
        
    }
}

class User {
    private int age;
    private String  name;

    

    public User() {
    }

    public User(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    
}