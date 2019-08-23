class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        _positive = True
        if n < 0:
            _positive = False
            n = -n
        _pow_result = self.normal_pow(x, n)
        if _positive == False:
            return 1/_pow_result
        return _pow_result

    def normal_pow(self, x: float, n: int):
        if n == 1:
            return x
        if n == 2:
            return x * x
        _r = n % 2
        if _r == 0:
            _A = self.normal_pow(x, n/2)
            return _A * _A
        if _r == 1:
            _A = self.normal_pow(x, (n-1)/2)
            return _A * _A * x


Sol = Solution()
test_x = 2
test_n = 10
test_result = Sol.myPow(test_x, test_n)
print('result:', test_result)