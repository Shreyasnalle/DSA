class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        if n == 0 :
            return False
        m = len(board[0])
        if len(word) > n * m :
            return False
        def helper(board, word, i, j, n, m, k) :
            if k == len(word) :
                return True
            if i < 0 or i >= n or j < 0 or j >= m :
                return False
            if word[k] != board[i][j] :
                return False
            temp = board[i][j]
            board[i][j] = '#'
            x = [0, 0, -1, 1]
            y = [-1, 1, 0, 0]
            found = False
            for index in range(4):
                found = found or helper(board, word, i + x[index], j + y[index], n, m, k + 1)
            board[i][j] = temp
            return found
        for i in range(n) :
            for j in range(m) :
                if word[0] == board[i][j] :
                    if helper(board, word, i, j, n, m, 0) :
                        return True
        return False