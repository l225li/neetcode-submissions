class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_val = 0
        hashmap = {0 : 1}

        for num in nums:
            sum_val += num
            if sum_val - k in hashmap:
                count += hashmap[sum_val - k]
            hashmap[sum_val] = hashmap.get(sum_val, 0) + 1
        
        return count