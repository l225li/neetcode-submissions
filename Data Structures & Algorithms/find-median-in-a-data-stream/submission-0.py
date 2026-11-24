class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)
        heapq.heappush(self.maxheap, - heapq.heappop(self.minheap))
        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, - heapq.heappop(self.maxheap))
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2.0
        return - self.maxheap[0]
        
        