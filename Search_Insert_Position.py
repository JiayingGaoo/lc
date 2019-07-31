class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        i = 0
        if target < nums[0]:
            return 0
        if target == nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) - 1
        while i < len(nums) - 1:
            if target >= nums[i] and target <= nums[i+1]:
                print(nums[i], nums[i+1])
                if target == nums[i]:
                    return i
                return i + 1
            i = i + 1

test_list = [1, 3]
test_target_int = 3
Sol = Solution()
print(Sol.searchInsert(test_list, test_target_int))
