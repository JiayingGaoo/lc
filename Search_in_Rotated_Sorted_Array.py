class Solution:
    def search(self, nums: list, target: int) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        if len_nums == 1:
            if target == nums[0]:
                return 0
            return -1
        if target == nums[0]:
            return 0
        if target == nums[len_nums-1]:
            return len_nums-1

        if target < nums[0]:
            for i in range(len_nums - 1, -1, -1):
                if nums[i] == target:
                    return i
                if i > 0 and nums[i] < nums[i - 1]:
                    return -1

        if target > nums[len_nums - 1]:
            for i in range(0, len_nums):
                if nums[i] == target:
                    return i
                if i < len_nums - 1 and nums[i] > nums[i + 1]:
                    return -1

        if target < nums[len_nums - 1] and target > nums[0]:
            for i in range(1, len_nums - 1):
                if nums[i] == target:
                    return i
        return -1


test_list = [1, 3, 5]
test_target = 3
Sol = Solution()
test_result = Sol.search(test_list, test_target)
print(test_result)