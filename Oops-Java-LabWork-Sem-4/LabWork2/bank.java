import java.util.Scanner;

class bank{
    double balance;
    int username;
    int password; 
    bank(double balance, int username, int password){
        this.
    }
    public static void main(String[] args){
        System.out.println("Enter amount to be Debited: ");
        Scanner s = new Scanner();
        double debitAmount = s.nextDouble();
        debit(debitAmount);
    }
    public static void debit(double money){
        if (CurrentState.balance > money){
            CurrentState.balance -= money;
        }else{
            System.out.println("Insufficient balance");
        }
    }
}