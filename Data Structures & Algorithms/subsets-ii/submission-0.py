class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(startIndex, path, used):
            res.append(path.copy())

            for i in range(startIndex,len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(i + 1, path, used)
                path.pop()
                used[i] = False
        
        backtrack(0, [], used)
        return res