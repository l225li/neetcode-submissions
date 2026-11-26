class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = [0] * numCourses
        pre = [[] for _ in range(numCourses)]

        for i, j in prerequisites:
            degrees[i] += 1
            pre[j].append(i)
        
        q = deque()
        for i, degree in enumerate(degrees):
            if degree == 0:
                q.append(i)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for x in pre[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    q.append(x)
        
        return ans if len(ans) == numCourses else []