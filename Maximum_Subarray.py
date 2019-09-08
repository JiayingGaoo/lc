class Solution:
    def maxSubArray(self, nums: list) -> int:
        len_nums = len(nums)
        max_sum = nums[0]
        i = 0
        while i < len_nums:
            _sum = nums[i]
            if _sum > max_sum:
                max_sum = _sum
            j = i + 1
            while j < len_nums:
                _sum = _sum + nums[j]
                if _sum > max_sum:
                    max_sum = _sum
                j = j + 1
            i = i + 1
        return max_sum

    def maxSubArray_1(self, nums: list) -> int:
        len_nums = len(nums)
        max_sum = nums[0]
        i = 0
        while i < len_nums:

            _sum = nums[i]
            if _sum > max_sum:
                max_sum = _sum
            j = i + 1
            while j < len_nums:
                _sum = _sum + nums[j]
                if _sum > max_sum:
                    max_sum = _sum
                j = j + 1

            i = i + 1
            while i < len_nums:
                _sum = _sum - nums[i - 1]
                if _sum > max_sum:
                    max_sum = _sum
                i = i + 1

        return max_sum



test_nums = [-2,1,-3,4,-1,2,1,-5,4]
Sol = Solution()
test_max = Sol.maxSubArray(test_nums)
print(test_max)

