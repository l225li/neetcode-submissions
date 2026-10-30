class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (target + total) % 2 != 0:
            return 0
        total_sum = (target + total) // 2
        dp = [0] * (total_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(total_sum, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[total_sum] 