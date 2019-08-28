class Solution:
    def count(self, nums: list) -> dict:
        count_dict = {}
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] = count_dict[num] + 1
            else:
                count_dict[num] = 1
        return count_dict

    def permuteUnique(self, nums: list) -> list:
        # count dict:
        count_dict = self.count(nums)
        # print(count_dict)

        len_for_each_list_in_cur_lists = 0
        len_nums = len(nums)
        cur_lists = []
        _base = sorted(nums)
        # print(_base)
        while len_for_each_list_in_cur_lists < len_nums:
            cur_lists, len_for_each_list_in_cur_lists = self.update_cur_lists(cur_lists, len_for_each_list_in_cur_lists,
                                                                              nums, len_nums, count_dict)

        result = []
        for cur_list in cur_lists:
            if sorted(cur_list) == _base:
                result.append(cur_list)
        return result

    def update_cur_lists(self, cur_lists: list, len_for_each_list_in_cur_lists: int, ori_list: list, len_ori: int, count_dict: dict) -> list:
        update_cur_list = []
        if len_for_each_list_in_cur_lists == 0:
            for i in range(len_ori):
                update_cur_list.append([ori_list[i]])
            return update_cur_list, 1

        for _cur_list in cur_lists:
            for i in range(len_ori):
                _temp = _cur_list[0:]
                _temp.append(ori_list[i])
                _item_num = 1
                for _cur_item in _cur_list:
                    if _cur_item == ori_list[i]:
                        _item_num = _item_num + 1

                if _temp not in update_cur_list and _item_num <= count_dict[ori_list[i]]:
                    update_cur_list.append(_temp)
        return update_cur_list, (len_for_each_list_in_cur_lists + 1)


test_ori_list = [1,1,0,0,1,-1,-1,1]
Sol = Solution()
# test_result = Sol.update_cur_lists([[1], [1], [2]], 1, test_ori_list, 3)
# print(test_update_list, test_update_len)
test_result = Sol.permuteUnique(test_ori_list)
print(test_result)