class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        node = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if not node.children[index]:
                newNode = TrieNode()
                node.children[index] = newNode
            node = node.children[index]
        node.isWord = True

    def search(self, word: str) -> bool:
        if not word:
            return True
        node = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            node = node.children[index]
            if not node:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        node = self.root
        for i, c in enumerate(prefix):
            index = ord(c) - ord('a')
            node = node.children[index]
            if not node:
                return False
        return True
        
        