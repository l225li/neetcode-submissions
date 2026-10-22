class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(startIndex, total, path):
            if total == target:
                res.append(path.copy())
            if total >= target:
                return
            
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                total += nums[i]
                backtrack(i, total, path)
                total -= nums[i]
                path.pop()
        backtrack(0, 0, [])
        return res