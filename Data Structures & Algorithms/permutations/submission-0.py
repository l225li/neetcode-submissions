class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
            if len(path) >= len(nums):
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        backtrack([], used)
        return res