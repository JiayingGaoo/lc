class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums = sorted(nums)
        len_nums = len(nums)
        if len_nums < 4:
            return []
        if len_nums == 4:
            _sum = sum(nums)
            if _sum == target:
                return [nums]
            else:
                return []
        if (nums[0] + nums[1] + nums[2] + nums[3]) > target or (nums[len_nums-4] + nums[len_nums-3] + nums[len_nums-2] + nums[len_nums-1]) < target:
            return []

        two_sum_list = []
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                _two_sum = nums[i] + nums[j]
                two_sum_list.append([_two_sum, i, j])
                if _two_sum > target and nums[j] >= 0:
                    break

        # len_two_num_list = len(two_sum_list)
        # # sort the two_sum_list according to the [0] value
        # for current_rank_id in range(len_two_num_list):
        #     min_val = two_sum_list[current_rank_id][0]
        #     _min_val_id = current_rank_id
        #     for candidate_id in range(current_rank_id + 1, len_two_num_list):
        #         if two_sum_list[candidate_id][0] <= min_val:
        #             min_val = two_sum_list[candidate_id][0]
        #             _min_val_id = candidate_id
        #     # arrange the order between _min_val_id and current_rank_id
        #     temp = two_sum_list[current_rank_id]
        #     two_sum_list[current_rank_id] = two_sum_list[_min_val_id]
        #     two_sum_list[_min_val_id] = temp

        three_sum_list = []
        for _two_sum in two_sum_list:
            i = _two_sum[2] + 1
            while i < len_nums:
                _three_sum = _two_sum[0] + nums[i]
                three_sum_list.append([_three_sum, _two_sum[1], _two_sum[2], i])
                if _three_sum > target and nums[i] >= 0:
                    break
                i = i + 1

        four_sum_list = []
        for _three_sum in three_sum_list:
            i = _three_sum[3] + 1
            while i < len_nums:
                _four_sum = _three_sum[0] + nums[i]
                if _four_sum == target:
                    _candidate = [nums[_three_sum[1]], nums[_three_sum[2]], nums[_three_sum[3]], nums[i]]
                    _candidate = sorted(_candidate)
                    if _candidate not in four_sum_list:
                        four_sum_list.append(_candidate)
                if _four_sum > target and nums[i] >= 0:
                    break
                i = i + 1
        return four_sum_list


test_list = [-500,-481,-480,-469,-437,-423,-408,-403,-397,-381,-379,-377,-353,-347,-337,-327,-313,-307,-299,-278,-265,-258,-235,-227,-225,-193,-192,-177,-176,-173,-170,-164,-162,-157,-147,-118,-115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,74,93,101,104,105,112,112,116,129,133,146,152,157,158,166,177,183,186,220,263,273,320,328,332,356,357,363,372,397,399,420,422,429,433,451,464,484,485,498,499]
test_list = [-499,-486,-479,-462,-456,-430,-415,-413,-399,-381,-353,-349,-342,-337,-336,-331,-330,-322,-315,-280,-271,-265,-249,-231,-226,-219,-216,-208,-206,-204,-188,-159,-144,-139,-123,-115,-99,-89,-80,-74,-61,-22,-22,-8,-5,4,43,65,82,86,95,101,103,123,149,152,162,165,168,183,204,209,209,220,235,243,243,244,248,253,260,273,281,284,288,290,346,378,382,384,407,411,423,432,433,445,470,476,497]
test_list = [-490,-481,-471,-467,-453,-450,-446,-440,-437,-424,-423,-391,-384,-373,-358,-332,-318,-314,-311,-309,-299,-279,-270,-257,-243,-208,-205,-171,-153,-147,-142,-138,-129,-99,-20,-19,17,30,44,82,86,93,122,125,138,139,158,169,175,181,199,200,203,203,205,225,248,272,277,306,334,335,337,338,342,344,359,396,403,405,412,434,437,439,440,441,443,446,446,457,465,468,473,496]

test_list = [-3,-2,-1,0,0,1,2,3]
test_target = 0
Sol = Solution()
test_solution_list = Sol.fourSum(test_list, test_target)
print(test_solution_list)