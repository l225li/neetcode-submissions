class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        res = []
        if not digits:
            return res
        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
            if index >= len(digits):
                return
            for c in letterMap[int(digits[index])]:
                path += c
                backtrack(index + 1, path)
                path = path[:-1]
        backtrack(0, "")
        return res