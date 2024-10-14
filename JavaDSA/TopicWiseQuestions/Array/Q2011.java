class Q2011{
    public void finalValueAfterOperations(String[] operations) {
        int answer = 0;
        for (String symbol : operations) {
            answer += (44 - symbol.charAt(1));
        }
        System.out.println(answer);
    }
}