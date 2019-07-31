class Solution:
    def reverse(self, x: int) -> int:
        input_str = str(x)
        input_list = list(input_str)
        neg = False
        if input_list[0] == '-':
            neg = True
            input_list.pop(0)

        len_input_list = len(input_list)
        for i in range(0, int(len_input_list / 2)):
            temp_val = input_list[i]
            input_list[i] = input_list[len_input_list - 1 - i]
            input_list[len_input_list - 1 - i] = temp_val

        if input_list[0] == '0' and len(input_list) > 1:
            input_list.pop(0)

        # convert the list(str) to int
        sum_str = ''
        if neg:
            sum_str = '-'
        for i in input_list:
            sum_str = sum_str + i
        int_sum_str = int(sum_str)
        if abs(int_sum_str) > pow(2, 31):
            return 0
        return int_sum_str


Sol = Solution()
Sol.reverse(0)