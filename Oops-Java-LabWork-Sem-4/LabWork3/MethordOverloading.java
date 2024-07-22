class MethordOverloading{
    public static int add(int n1, int n2, int n3){
        return n1 + n2 - n3;
    }
    public static int add(int n1, int n2){
        return n1 + n2;
    }
    public static int add(int n1){
        return n1;
    }
    public static void main(String[] args){
        MethordOverloading obj = new MethordOverloading();
        int rtn = obj.add(3);
        System.out.println(rtn);
    }
}