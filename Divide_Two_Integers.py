class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        thr_1 = pow(2, 31) - 1
        thr_0 = -pow(2, 31)
        sign_dividend = 1
        sign_divisor = 1
        if dividend < 0:
            sign_dividend = -1
            dividend = -dividend
        if divisor < 0:
            sign_divisor = -1
            divisor = -divisor

        # some specific case, the result can be straightly obtained
        if divisor > dividend:
            return 0
        if divisor == dividend:
            if (sign_dividend + sign_divisor) == 0:
                return -1
            return 1
        # must satisfy: divisor < dividend
        if divisor == 1:
            if (sign_dividend + sign_divisor) == 0:
                _result = -dividend
            else:
                _result = dividend
        else:
            _result = self.divide_key(dividend, divisor)
            if (sign_dividend + sign_divisor) == 0:
                _result = -_result

        if _result > thr_1:
            return thr_1
        if _result < thr_0:
            return thr_0
        return _result

    def divide_key(self, dividend: int, divisor: int) -> int:
        _output = 0
        cur_dividend_str = str(dividend)
        while int(cur_dividend_str) > divisor:
            # print('cur_dividend_str:', cur_dividend_str)
            _str = ''
            for i in range(len(cur_dividend_str)):
                _str = _str + cur_dividend_str[i]
                _int = int(_str)
                if _int >= divisor:
                    # print('_int = ', _int)
                    # get the temp _output int:
                    _o = 0
                    _sum = 0
                    while _sum <= _int:
                        _sum = _sum + divisor
                        _o = _o + 1
                    _o = _o - 1
                    # print('_o = ', _o)
                    _remain = divisor - (_sum - _int)
                    # print('_remain = ', _remain)
                    # check how many 0 need to be added after _o:
                    _str_o = str(_o)
                    _remain_str = str(_remain)
                    for j in range(i + 1, len(cur_dividend_str)):
                        _str_o = _str_o + '0'
                        _remain_str = _remain_str + cur_dividend_str[j]
                    # print('_str_o:', _str_o)
                    _output = _output + int(_str_o)
                    cur_dividend_str = _remain_str
                    break
        return _output

Sol = Solution()
# test_output = Sol.divide_key(10000000, 2)
# print('test_output = ', test_output)
test_quotient = Sol.divide(7, -3)
print(test_quotient)
# print('2147xxxxxx/2 = ', 2147483647/2)
# print('pow(2, 31) = ', pow(2, 31))
