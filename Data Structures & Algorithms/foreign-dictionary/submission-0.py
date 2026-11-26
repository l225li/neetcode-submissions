class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break 
        
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)

