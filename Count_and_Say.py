class Change_item:
    # three members: change_start_id: int, change_num: int, change_result: str
    def __init__(self):
        self.start_index_in_ori_list = -1
        self.end_index_in_ori_list = -1
        self.update_result = ''

class Solution:
    def str_update(self, input_str: str) -> str:
        output_str = ''
        i = 0
        while i < len(input_str):
            # i represents the current char index in input_str
            same_count = 1
            j = i + 1
            while j < len(input_str):
                if input_str[i] == input_str[j]:
                    same_count = same_count + 1
                else:
                    break
                j = j + 1
            output_str = output_str + str(same_count) + input_str[i]
            i = i + same_count
        return output_str

    def str_update_per_step(self, input_str: str) -> str:
        input_len = len(input_str)
        expected_sum = int(input_len * (input_len - 1) / 2)
        # print('expected_sum = ', expected_sum)
        i_find_list = []
        change_item_list = []
        while 1:
            i_find = input_str.find('2')
            if i_find >= 0 and i_find not in i_find_list:
                i_find_list.append(i_find)
                temp_change_item = Change_item()
                temp_change_item.update_result = '12'
                temp_change_item.start_index_in_ori_list = i_find
                temp_change_item.end_index_in_ori_list = i_find
                change_item_list.append(temp_change_item)
            i_find = input_str.find('11')
            if i_find >= 0 and i_find not in i_find_list:
                i_find_list.append(i_find)
                i_find_list.append(i_find + 1)
                temp_change_item = Change_item()
                temp_change_item.update_result = '21'
                temp_change_item.start_index_in_ori_list = i_find
                temp_change_item.end_index_in_ori_list = i_find + 1
                change_item_list.append(temp_change_item)
            i_find = input_str.find('1')
            if i_find >= 0 and i_find not in i_find_list:
                i_find_list.append(i_find)
                temp_change_item = Change_item()
                temp_change_item.update_result = '11'
                temp_change_item.start_index_in_ori_list = i_find
                temp_change_item.end_index_in_ori_list = i_find
                change_item_list.append(temp_change_item)

            # print(i_find_list)
            if sum(i_find_list) == expected_sum:
                print('calculate the output_str:', end='')
                # calculate the output_str:
                output_str = ''
                while len(change_item_list) > 0:
                    min_start_index = change_item_list[0].start_index_in_ori_list
                    update_str = change_item_list[0].update_result
                    select_id = 0
                    for i, temp_change_item in enumerate(change_item_list):
                        if temp_change_item.start_index_in_ori_list <= min_start_index:
                            min_start_index = temp_change_item.start_index_in_ori_list
                            update_str = change_item_list[i].update_result
                            select_id = i
                    output_str = output_str + update_str
                    change_item_list.pop(select_id)
                break
        print(output_str)
        return output_str

    def countAndSay(self, n: int) -> str:
        i = 1
        _str = '1'
        while i < n:
            i = i + 1
            _str = self.str_update_per_step(_str)
        print(_str)
        return _str


test_change = Change_item()
Sol = Solution()
test_output = Sol.str_update('111221')
print(test_output)
# Sol.str_update_per_step('1211')
# Sol.countAndSay(5)