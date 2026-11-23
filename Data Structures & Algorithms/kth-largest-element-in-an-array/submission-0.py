class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums[:k]
        heapq.heapify(q)

        for i in range(k, len(nums)):
            if nums[i] > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, nums[i])
        return heapq.heappop(q)