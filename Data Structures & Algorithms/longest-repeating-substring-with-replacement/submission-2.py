class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        maxf = 0

        for r, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            maxf = max(maxf, count[c])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res