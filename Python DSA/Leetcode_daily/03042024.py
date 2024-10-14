from collections import defaultdict

board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]]
word = "SEE"

class Solution:
    def exist(self, board, word) -> bool:
        # finding first letter 
        positions = defaultdict(list)
        m, n = len(board), len(board[0])
        for letter in word:
            positions[letter] = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == letter:
                        positions[letter].append((i,j))
        print(positions)
        rtn = False
        noOfCharacters, index = len(word), 0
        for initial in positions[word[0]]:
            i, j = initial
            posiblePositions = set((i ,j + 1),
                                    (i + 1 ,j),
                                    (i ,j - 1),
                                    (i - 1 ,j))
            while index < noOfCharacters:
                nextIndex = 



sol = Solution().exist(board, word)
