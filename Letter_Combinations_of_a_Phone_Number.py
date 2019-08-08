class Solution:
    def two_letterlist_combination(self, base_list: list, append_list: list) -> list:
        update_list = []
        if len(base_list) == 0:
            return append_list
        for _base in base_list:
            for _append in append_list:
                temp_str = _base + _append
                update_list.append(temp_str)
        return update_list

    def digit_to_letterlist(self, digit: str) -> list:
        if digit == '1':
            return []
        if digit == '2':
            return ['a', 'b', 'c']
        if digit == '3':
            return ['d', 'e', 'f']
        if digit == '4':
            return ['g', 'h', 'i']
        if digit == '5':
            return ['j', 'k', 'l']
        if digit == '6':
            return ['m', 'n', 'o']
        if digit == '7':
            return ['p', 'q', 'r', 's']
        if digit == '8':
            return ['t', 'u', 'v']
        if digit == '9':
            return ['w', 'x', 'y', 'z']

    def letterCombinations(self, digits: str) -> list:
        len_str = len(digits)
        current_list = []
        for i in range(len_str):
            append_list = self.digit_to_letterlist(digits[i])
            current_list = self.two_letterlist_combination(current_list, append_list)
        print(current_list)
        return current_list

test_str = '23456789'
Sol = Solution()
test_letter_combinations = Sol.letterCombinations(test_str)