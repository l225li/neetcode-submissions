class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = ['.' * n for _ in range(n)]

        def backtrack(row, path):
            if row == n:
                res.append(path.copy())
                return
            
            for col in range(n):
                if self.isValid(row, col, path):
                    path[row] = path[row][:col] + 'Q' + path[row][col+1:]
                    backtrack(row + 1, path)
                    path[row] = path[row][:col] + '.' + path[row][col+1:]
        backtrack(0, path)
        return res
    def isValid(self, row, col, path):
        for i in range(row):
            if path[i][col] == 'Q':
                return False
        
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if path[i][j] == 'Q':
                return False 
            i -= 1
            j -= 1
        
        i, j = row - 1, col + 1
        while i >= 0 and j < len(path):
            if path[i][j] == 'Q':
                return False 
            i -= 1
            j += 1
        
        return True