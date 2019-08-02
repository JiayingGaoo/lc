class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cur_column_id = 0
        wrote_start_index = 0
        wrote_end_index = len(s)
        list_total = []
        if wrote_end_index == 0:
            return ''
        if wrote_end_index == 1 or numRows == 1:
            return s

        while 1:
            cur_column_list = []
            for i in range(0, numRows):
                cur_column_list.append('')
            cur_mod = cur_column_id % (numRows - 1)
            if cur_mod == 0:
                # then, each space of this list should be wrote a char
                temp_id = 0
                for i in range(wrote_start_index, wrote_end_index):
                    cur_column_list[temp_id] = s[i]
                    temp_id = temp_id + 1
                    if temp_id == numRows:
                        # the list reach the end
                        wrote_start_index = i + 1
                        break

            else:
                # then, only one space of this list should be wrote a char
                cur_column_list[numRows - cur_mod - 1] = s[wrote_start_index]
                wrote_start_index = wrote_start_index + 1

            # print(cur_column_list)
            list_total.append(cur_column_list)
            cur_column_id = cur_column_id + 1
            if cur_mod == 0 and cur_column_list[-1] == '':
                break
            if wrote_start_index == wrote_end_index:
                break

        str_result = ''
        for _index in range(0, numRows):
            for _list_id in range(0, cur_column_id):
                str_result = str_result + list_total[_list_id][_index]

        return str_result

test_str = "ABC"
test_numrows = 2
Sol = Solution()
test_result = Sol.convert(test_str, test_numrows)
print(test_result)