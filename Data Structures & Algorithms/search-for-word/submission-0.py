class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def backtrack(r, c, i):
            if not 0 <= r < n or not 0 <= c < m or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            board[r][c] = ''
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c - 1, i + 1) or
                   backtrack(r, c + 1, i + 1))
            board[r][c] = word[i]
            return res
        for i in range(n):
            for j in range(m):
                if backtrack(i, j , 0):
                    return True
        return False