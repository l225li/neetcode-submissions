class TrieNode:
    def __init__(self):
        self.isWord = False
        self.word = None
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        if not word:
            return
        cur = self.root
        for char in word:
            c = ord(char) - ord('a')
            if not cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        cur.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        n, m = len(board), len(board[0])
        result = set()
        visited = [[False] * m for _ in range(n)]

        def search(trieNode, x, y):
            if trieNode.isWord:
                result.add(trieNode.word)
            visited[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    index = ord(board[nx][ny]) - ord('a')
                    if trieNode.children[index]:
                        search(trieNode.children[index], nx, ny)
            visited[x][y] = False
        for i in range(n):
            for j in range(m):
                c = ord(board[i][j]) - ord('a')
                if trie.root.children[c]:
                    search(trie.root.children[c], i, j)
        return list(result)