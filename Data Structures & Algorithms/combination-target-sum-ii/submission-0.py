class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        used = [False] * len(candidates)
        def backtrack(startIndex, total, path, used):
            if total == target:
                res.append(path.copy())
            if total >= target:
                return
            
            for i in range(startIndex, len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                    continue
                total += candidates[i]
                path.append(candidates[i])
                used[i] = True
                backtrack(i + 1, total, path, used)
                used[i] = False
                path.pop()
                total -= candidates[i]
        backtrack(0, 0, [], used)
        return res