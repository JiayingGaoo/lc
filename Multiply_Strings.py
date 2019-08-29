class Solution:
    def single_str_to_int(self, num: str) -> int:
        if num == '0':
            return 0
        if num == '1':
            return 1
        if num == '2':
            return 2
        if num == '3':
            return 3
        if num == '4':
            return 4
        if num == '5':
            return 5
        if num == '6':
            return 6
        if num == '7':
            return 7
        if num == '8':
            return 8
        if num == '9':
            return 9

    def single_float_to_str(self, num: float) -> str:
        if num == 0.0:
            return '0'
        if num == 1.0:
            return '1'
        if num == 2.0:
            return '2'
        if num == 3.0:
            return '3'
        if num == 4.0:
            return '4'
        if num == 5.0:
            return '5'
        if num == 6.0:
            return '6'
        if num == 7.0:
            return '7'
        if num == 8.0:
            return '8'
        if num == 9.0:
            return '9'


    def single_multiply(self, num1: str, pow_num1: int, num2: str, pow_num2: int) -> int:
        _int_num1 = self.single_str_to_int(num1)
        _int_num2 = self.single_str_to_int(num2)
        _int_mul = _int_num1 * _int_num2
        _pow_num = pow_num1 + pow_num2
        return _int_mul, _pow_num

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1
        len_num1 = len(num1)
        len_num2 = len(num2)
        _sum = 0
        _pow_count_dict = {}
        for i in range(len_num1):
            _temp_str_num1 = num1[i]
            _pow_num1 = len_num1 - i - 1
            for j in range(len_num2):
                _temp_str_num2 = num2[j]
                _pow_num2 = len_num2 - j - 1
                _int, _pow = self.single_multiply(_temp_str_num1, _pow_num1, _temp_str_num2, _pow_num2)
                if _pow in _pow_count_dict:
                    _pow_count_dict[_pow] = _pow_count_dict[_pow] + _int
                else:
                    _pow_count_dict[_pow] = _int

        # print('_pow_count_dict:', _pow_count_dict)
        max_pow = max(_pow_count_dict.keys())
        _k = 0
        while _k <= max_pow:
            if _pow_count_dict[_k] >= 10:
                _ori = _pow_count_dict[_k]
                _pow_count_dict[_k] = _pow_count_dict[_k] % 10
                if _k == max_pow:
                    _pow_count_dict[_k + 1] = (_ori - _pow_count_dict[_k]) / 10
                    max_pow = max_pow + 1
                else:
                    _pow_count_dict[_k + 1] = _pow_count_dict[_k + 1] + (_ori - _pow_count_dict[_k]) / 10
            _k = _k + 1
        # print('update_pow_count_dict:', _pow_count_dict)
        _result = ''
        for _k in range(max_pow, -1, -1):
            _result = _result + self.single_float_to_str(_pow_count_dict[_k])
        # print('result:', _result)
        return _result

test_str_num1 = '9'
test_str_num2 = '22'
Sol = Solution()
Sol.multiply(test_str_num1, test_str_num2)

