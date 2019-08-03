class Solution:
    def intToRoman(self, num: int) -> str:
        _to_str = str(num)
        _len = len(_to_str)
        if _len == 4:
            _str_pro = _to_str
        if _len < 4:
            _str_pro = ''
            for i in range(0, 4 - _len):
                _str_pro = _str_pro + '0'
            _str_pro = _str_pro + _to_str
            _len = 4
        print(_str_pro, _len)

        i = 0
        roman_list = []
        while i < _len:
            print('i = ', i)
            if i == 0:  # combination of I and V, X
                base_1 = 'I'
                base_2 = 'V'
                base_3 = 'X'
            if i == 1:  # combination of X and L, C
                base_1 = 'X'
                base_2 = 'L'
                base_3 = 'C'
            if i == 2:  # combination of L and C, D
                base_1 = 'C'
                base_2 = 'D'
                base_3 = 'M'
            if i == 3:  # combination of C and D, M
                base_1 = 'M'
                base_2 = '-'
                base_3 = '-'

            cur_int = int(_str_pro[_len - i - 1])
            print('current_int = ', cur_int)
            temp_str = ''
            if cur_int < 4:
                temp_str = ''
                for _i in range(0, cur_int):
                    temp_str = temp_str + base_1
            if cur_int == 4:
                temp_str = base_1 + base_2
            if cur_int > 4 and cur_int < 9:
                temp_str = base_2
                for _i in range(0, cur_int - 5):
                    temp_str = temp_str + base_1
            if cur_int == 9:
                temp_str = base_1 + base_3
            print('temp_str = ', temp_str)
            roman_list.append(temp_str)
            i = i + 1

        print('roman_list = ', roman_list)
        roman_str = ''
        for i in range(len(roman_list) - 1, -1, -1):
            roman_str = roman_str + roman_list[i]
        return roman_str

test_int = 58
Sol = Solution()
test_roman = Sol.intToRoman(test_int)
print(test_roman)