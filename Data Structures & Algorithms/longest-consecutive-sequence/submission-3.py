class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_len = 0

        for num in numset:
            if num - 1 not in numset:
                current_num = num
                current_len = 1
                while current_num + 1 in numset:
                    current_num += 1
                    current_len += 1
                max_len = max(max_len, current_len)
            
        return max_len