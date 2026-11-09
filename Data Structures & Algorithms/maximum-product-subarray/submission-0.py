class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = result = nums[0]

        for num in nums[1:]:
            candidates = (num, curr_max * num, curr_min * num)
            curr_max = max(candidates)
            curr_min = min(candidates)
            result = max(result, curr_max)
        return result