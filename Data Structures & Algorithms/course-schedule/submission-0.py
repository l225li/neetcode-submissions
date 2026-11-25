class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses
        pre = [[] for _ in range(numCourses)]

        for i, j in prerequisites:
            degrees[i] += 1
            pre[j].append(i)
        
        cur = []
        for i, degree in enumerate(degrees):
            if degree == 0:
                cur.append(i)
        ans = []
        while cur:
            next = []
            for i in cur:
                for x in pre[i]:
                    degrees[x] -= 1
                    if degrees[x] == 0:
                        next.append(x)
            ans += cur
            cur = next
        return len(ans) == numCourses