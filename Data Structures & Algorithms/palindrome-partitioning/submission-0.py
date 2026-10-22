class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(startIndex, path):
            if startIndex == len(s):
                res.append(path.copy())
            if startIndex >= len(s):
                return
            for i in range(startIndex, len(s)):
                if self.is_pali(s, startIndex, i):
                    path.append(s[startIndex:i + 1])
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, [])
        return res
    
    def is_pali(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True