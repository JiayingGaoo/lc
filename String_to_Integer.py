class Solution:
    def myAtoi(self, s: str) -> int:
        input_list_pro = list(s)
        # find the first digit block
        i = 0
        digit_block_start = -1
        while i < len(input_list_pro):
            if digit_block_start == -1 and input_list_pro[i] == '.':
                return 0
            try:
                _convert = int(input_list_pro[i])
                if digit_block_start == -1 and _convert!= 0:
                    digit_block_start = i
                    break
            except:
                if digit_block_start == -1:
                    if input_list_pro[i] != '+' and input_list_pro[i] != '-' and input_list_pro[i] != ' ':
                        return 0
            i = i + 1

        if digit_block_start == -1:
            return 0

        digit_block_end = len(input_list_pro)
        for i in range(digit_block_start + 1, len(input_list_pro)):
            if input_list_pro[i] == '.':
                digit_block_end = i
                break
            try:
                _convert = int(input_list_pro[i])
            except:
                digit_block_end = i
                break
        print(digit_block_start, digit_block_end)

        digit_str = ''
        for i in range(digit_block_start, digit_block_end):
            digit_str = digit_str + input_list_pro[i]
        digit_part = int(digit_str)
        print('digit_part = ', digit_part)

        _add_count = 0
        _minus_count = 0
        _zero_count = 0
        first_zero_id = len(input_list_pro)
        first_minus_id = len(input_list_pro)
        first_add_id = len(input_list_pro)
        for i in range(0, digit_block_start):
            if input_list_pro[i] == '0':
                if first_zero_id == len(input_list_pro):
                    first_zero_id = i
                _zero_count = _zero_count + 1
            if input_list_pro[i] == '+':
                if first_add_id == len(input_list_pro):
                    first_add_id = i
                _add_count = _add_count + 1
            if input_list_pro[i] == '-':
                if first_minus_id == len(input_list_pro):
                    first_minus_id = i
                _minus_count = _minus_count + 1
            if _add_count > 1 or _minus_count > 1:
                return 0
            if _add_count >= 1 and _minus_count >= 1:
                return 0

        for i in range(first_minus_id, digit_block_start):
            if input_list_pro[i] == ' ':
                return 0

        for i in range(first_add_id, digit_block_start):
            if input_list_pro[i] == ' ':
                return 0

        for i in range(first_zero_id, digit_block_start):
            if input_list_pro[i] == ' ' or input_list_pro[i] == '+' or input_list_pro[i] == '-':
                return 0

        sign = 1
        if _minus_count == 1:
            sign = -1

        digit = digit_part * sign
        if sign >= 0:
            if digit < pow(2, 31):
                return digit
            else:
                return pow(2, 31) - 1
        else:
            if digit > -pow(2, 31):
                return digit
            else:
                return -pow(2, 31)


test_str = "  321"
Sol = Solution()
test_output_int = Sol.myAtoi(test_str)
print("result: ", test_output_int)