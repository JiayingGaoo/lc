class Solution:
    def gcd(self, a: int, b: int):
        if a < b:
            temp = a
            a = b
            b = temp

        while 1:
            c = a % b
            if c == 0:
                return b
            a = b
            b = c


Sol = Solution()
test_gcb = Sol.gcd(100, 80)
print(test_gcb)