class knightProbability {
    int onBoards = -1;
    int offBoard = 0;
    private void moves(int currentRow, int currentColumen, int n, int k, int counsumedk){
        if(currentColumen >= n || currentRow >= n || currentColumen < 0 || currentRow < 0){
            offBoard += 1;
            return;
        }
        else{
            onBoards += 1;
            System.out.println("On board");
        }
        if(counsumedk == k) return; 
        System.out.println(onBoards +" " + offBoard);

        moves(currentRow + 2, currentColumen - 1, n, k, counsumedk + 1);
        moves(currentRow + 2, currentColumen + 1, n, k, counsumedk + 1);
        moves(currentRow - 2, currentColumen - 1, n, k, counsumedk + 1);
        moves(currentRow - 2, currentColumen + 1, n, k, counsumedk + 1);
        moves(currentRow + 1, currentColumen - 2, n, k, counsumedk + 1);
        moves(currentRow - 1, currentColumen - 2, n, k, counsumedk + 1);
        moves(currentRow + 1, currentColumen + 2, n, k, counsumedk + 1);
        moves(currentRow - 1, currentColumen + 2, n, k, counsumedk + 1);

        return;
    }

    public double knightProbability(int n, int k, int row, int column) {
        moves(row, column, n, k, 0);   
        double val = onBoards/(onBoards + offBoard);
        return val;
    }

    public static void main(String[] args) {
        knightProbability obj =  new knightProbability();
        double an = obj.knightProbability(3, 2, 0, 0);
        System.out.println(an);
        return;
    }
}