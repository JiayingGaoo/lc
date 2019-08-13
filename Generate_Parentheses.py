class Solution:
    def add_one_parentheses_at_current_str(self, input_parentheses: str) -> list:
        len_str_input = len(input_parentheses)
        print(len_str_input)
        output_parentheses_str_list = []
        for i in range(len_str_input):
            _s = ''
            for j in range(i):
                _s = _s + input_parentheses[j]
            _s = _s + '()'
            for j in range(i, len_str_input):
                _s = _s + input_parentheses[j]
            print(_s)
            output_parentheses_str_list.append(_s)

        _s = input_parentheses + '()'
        output_parentheses_str_list.append(_s)
        return output_parentheses_str_list

    def parentheses_check(self, str_parentheses: str) -> bool:
        # print(str_parentheses)
        _to_list = list(str_parentheses)
        _len = len(_to_list)
        while len(_to_list) > 2:
            if _to_list[0] == ')':
                return False
            for i in range(0, _len - 1):
                if _to_list[i] == '(' and _to_list[i + 1] == ')':
                    _to_list.pop(i)
                    _to_list.pop(i)
                    break
            # print('update_list: ', _to_list)
        if _to_list[0] == '(' and _to_list[1] == ')':
            return True
        return False

    def generateParenthesis(self, n: int) -> list:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        if n == 2:
            return ['()()', '(())']
        _str_list = ['()()', '(())']
        i = 3
        while i <= n:
            current_output_list = []
            for _str in _str_list:
                _temp = self.add_one_parentheses_at_current_str(_str)
                for j in range(len(_temp)):
                    if _temp[j] not in current_output_list:
                        current_output_list.append(_temp[j])
            _str_list = current_output_list
            i = i + 1
        return current_output_list



Sol = Solution()
# test_parentheses = '()()'
# output_list = Sol.add_one_parentheses_at_current_str(test_parentheses)
# print(output_list)

test_solution_list = Sol.generateParenthesis(4)
print(test_solution_list)