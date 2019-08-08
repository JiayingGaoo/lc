class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums = sorted(nums)
        len_nums = len(nums)
        i = 0
        best_sum = nums[0] + nums[1] + nums[2]
        while i < len_nums:
            j = i + 1
            k = len_nums - 1
            while k > j:
                _sum = nums[i] + nums[j] + nums[k]
                if abs(_sum - target) < abs(best_sum - target):
                    best_sum = _sum
                if _sum > target:
                    k = k - 1
                if _sum < target:
                    j = j + 1
                if _sum == target:
                    return _sum
            i = i + 1
        return best_sum


test_list = [-1, 2, 1, -4]
test_target = 1
Sol = Solution()
test_best_sum = Sol.threeSumClosest(test_list, test_target)
print(test_best_sum)