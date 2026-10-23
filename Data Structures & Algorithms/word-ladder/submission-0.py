from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque([beginWord])
        visited = {beginWord}
        level = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                chars = list(word)
                for i in range(len(chars)):
                    original = chars[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original:
                            continue
                        chars[i] = c
                        next_word = "".join(chars)
                        if next_word in wordSet and next_word not in visited:
                            visited.add(next_word)
                            q.append(next_word)
                    chars[i] = original
            
            level += 1
        
        return 0