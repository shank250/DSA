import java.util.*;

class MyStack{
    List<Pair> stack ;
    MyStack(){
        this.stack = new ArrayList<Pair>();
    }
    
}

class Pair{
    int val;
    int curMin;
    Pair(int val, int curMin){
        this.val = val;
        this.curMin = curMin;
    }
}