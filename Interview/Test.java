class Test{
    public static void main(String[] atgs){
        int[] lst = new int[]{1, 2,3};
        (x) -> x**2;

    }
}
class Main {
    public static void main(String args[]) {
        ServiceNow s = new ServiceNow(5);
    }
}
class Interview{
    Interview(){
        System.out.println(" Welcome to Interview ");
    }
}
class ServiceNow extends Interview{
    ServiceNow(){
        System.out.println(" Welcome to  ");
    }
    ServiceNow(int x){
        super();
        // this();
        
        System.out.println(" Welcome to   Academy 2");
    }
}

select empName from (
Select empName, salary from emptable order by salary decs limit 3) 
order by salary acs limit 1;
    