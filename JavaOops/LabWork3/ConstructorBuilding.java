public class ConstructorBuilding{

    public ConstructorBuilding(){
    
        int x;
        System.out.println("Constructor");
        x = 1;
    }
    public static void main(String[] args) {
        // Creating and obj of class
        ConstructorBuilding classBuilder = new ConstructorBuilding();
        System.out.println("Value Initialized Using Constructor x : " + classBuilder.x);
    }
}

// CODE: super keyword ussage