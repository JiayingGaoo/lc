class Solution:
    def list_to_count_dict(self, nums: list) -> dict:
        # print(nums)
        count_dict = {}
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] = count_dict[num] + 1
            else:
                count_dict[num] = 1
        # print('dict_debug:', count_dict)
        return count_dict

    def permute(self, nums: list) -> list:
        len_nums = len(nums)
        len_for_each_list_in_cur_lists = 0
        current_lists = []
        ori_dict = self.list_to_count_dict(nums)
        while len_for_each_list_in_cur_lists < len_nums:
            current_lists, len_for_each_list_in_cur_lists = self.udpate_lists(current_lists,
                                                                              len_for_each_list_in_cur_lists,
                                                                              nums, len_nums, ori_dict)
        return current_lists

    def udpate_lists(self, current_lists: list, len_for_each_list_in_cur_lists: int, ori_list: list,
                     len_for_ori_list: int, ori_dict: dict) -> list:
        update_lists = []
        if len_for_each_list_in_cur_lists == 0:
            for i in range(len_for_ori_list):
                update_lists.append([ori_list[i]])
            return update_lists, 1

        for current_list in current_lists:
            _current_dict = self.list_to_count_dict(current_list)
            for _ori_element in ori_list:
                if _ori_element in _current_dict.keys():
                    _current_dict[_ori_element] = _current_dict[_ori_element] + 1
                else:
                    _current_dict[_ori_element] = 1
                if _current_dict[_ori_element] <= ori_dict[_ori_element]:
                    _temp = current_list[0:]
                    _temp.append(_ori_element)
                    if _temp not in update_lists:
                        update_lists.append(_temp)
        return update_lists, len_for_each_list_in_cur_lists + 1


test_nums = [1, 2, 3]
Sol = Solution()
test_result = Sol.permute(test_nums)
print(test_result)



