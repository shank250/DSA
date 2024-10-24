public class Factorial {
    private int number;
    // create getter setter or constructor
    Factorial(){
        this.number = -1;
    }
    Factorial(int number){
        this.number = number;
    }
    public int getNumber(){
        return this.number;
    }
    public  void setNumber(int num){
        this.number = num;
        return;
    }
    public int fact(int n){
        if(n == 1)
            return 1;
        return n*fact(n - 1);
    }
}

