class Solution:
    def pro_deplicate(self, nums: list) -> list:
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            same_count = 1
            j = i + 1
            while j < len_nums:
                if nums[j] == nums[i]:
                    same_count = same_count + 1
                    if (same_count == 3 and nums[i] != 0) or (same_count == 4 and nums[i] == 0):
                        # delete nums[j]
                        for k in range(j, len_nums - 1):
                            nums[k] = nums[k + 1]
                        len_nums = len_nums - 1
                        same_count = same_count - 1
                        j = j - 1
                j = j + 1
            i = i + 1
        return nums[0: len_nums]


    def threeSum(self, nums: list) -> list:
        nums = self.pro_deplicate(nums)
        nums.sort()
        print('sorted nums: ', nums)
        len_nums = len(nums)
        solution_list = []
        i = 0
        while i < (len_nums - 2):
            if nums[i] > 0:
                break
            j = i + 1
            k = len_nums - 1
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    if nums[k] == nums[k-1]:
                        k = k - 1
                    k = k - 1

                if sum < 0:
                    if nums[j] == nums[j+1]:
                        j = j + 1
                    j = j + 1


                if sum == 0:
                    solution_list.append([nums[i], nums[j], nums[k]])
                    # candidate_solution = [nums[i], nums[j], nums[k]]
                    # if candidate_solution not in solution_list:
                    #     solution_list.append(candidate_solution)
                    if nums[k] == nums[k-1] and nums[j] == nums[j+1]:
                        k = k - 1
                        j = j + 1
                    k = k - 1
                    j = j + 1
            if nums[i] == nums[i + 1]:
                i = i + 1
            i = i + 1
        return solution_list

test_list = [-4,-1,-4,0,2,-2,-4,-3,2,-3,2,3,3,-4]
Sol = Solution()
# test_sorted_list = Sol.sort_list(test_list)
# print(test_sorted_list)
test_solution_list = Sol.threeSum(test_list)
print(test_solution_list)
print(len(test_solution_list))

