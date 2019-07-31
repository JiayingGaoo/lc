class Solution:
    def removeDuplicates(self, nums: list) -> int:
        cur_id = 0
        repeat_num = 0
        while cur_id < len(nums):
            temp_id = cur_id + 1
            while temp_id < len(nums):
                if nums[cur_id] == nums[temp_id]:
                    # print(cur_id, nums[cur_id], ' VS ', temp_id, nums[temp_id])
                    repeat_num = repeat_num + 1
                    nums.pop(temp_id)
                    temp_id = temp_id - 1
                else:
                    break
                temp_id = temp_id + 1
            cur_id = cur_id + 1
        print(nums)
        return len(nums)



test_list = [1, 1, 2]
Sol = Solution()
Sol.removeDuplicates(test_list)