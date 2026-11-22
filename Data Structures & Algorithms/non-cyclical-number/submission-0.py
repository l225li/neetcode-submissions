class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            total = 0
            seen.add(n)

            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10 
            n = total
        return n == 1