"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maps = {}

        def dfs(node, maps):
            if not node:
                return None
            if node in maps:
                return maps[node]
            
            copy = Node(node.val)
            maps[node] = copy
            for child in node.neighbors:
                child_copy = dfs(child, maps)
                copy.neighbors.append(child_copy)
            return copy
        
        return dfs(node, maps)