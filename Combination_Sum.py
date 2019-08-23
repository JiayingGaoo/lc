class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        # all num are positive
        len_candidates = len(candidates)
        candidates.sort()
        if candidates[0] > target:
            return []
        if candidates[0] == target:
            return [[candidates[0]]]

        max_element_num_in_a_solution = int(target / candidates[0])
        # min_element_num_in_a_solution = 1
        # if candidates[len_candidates - 1] < target:
        #     min_element_num_in_a_solution = int(target / candidates[len_candidates - 1])

        min_element_num_in_a_solution = 1
        # print('max_element_num_in_a_solution = ', max_element_num_in_a_solution)
        # print('min_element_num_in_a_solution = ', min_element_num_in_a_solution)
        potential_add_num = min_element_num_in_a_solution
        update_candidate_list = []
        solution_list = []
        while potential_add_num <= max_element_num_in_a_solution:
            update_candidate_list = self.candidate_list_update(update_candidate_list, candidates, target)
            # print('update_candidate_list:',)
            # print(update_candidate_list)
            i = 0
            while i < len(update_candidate_list):
                if update_candidate_list[i][0] == target:
                    _solution = update_candidate_list[i][1:]
                    _solution.sort()
                    if _solution not in solution_list:
                        solution_list.append(_solution)
                        # print('obtain a solution:', _solution)
                        # delete the update_candidate_list[i] in update_candidate_list
                        update_candidate_list.pop(i)
                        i = i - 1
                elif update_candidate_list[i][0] > target:
                    update_candidate_list.pop(i)
                    i = i - 1
                i = i + 1
            potential_add_num = potential_add_num + 1

        return solution_list

    def candidate_list_update(self, cur_candidate_list: list, ori_candidates_list: list, target) -> list:
        update_candidate_list = []
        len_cur_candidate_list = len(cur_candidate_list)
        len_ori_candidate_list = len(ori_candidates_list)
        if len_cur_candidate_list == 0:
            for i in range(len_ori_candidate_list):
                update_candidate_list.append([ori_candidates_list[i], ori_candidates_list[i]])
            return update_candidate_list

        for i in range(len_cur_candidate_list):
            for j in range(len_ori_candidate_list):
                # print(cur_candidate_list[i])
                _temp = cur_candidate_list[i][0: len(cur_candidate_list[i])]
                _temp.append(ori_candidates_list[j])
                _temp[0] = _temp[0] + ori_candidates_list[j]
                if _temp[0] <= target:
                    update_candidate_list.append(_temp)

        return update_candidate_list


test_list = [6,8,12,5,9,3,4,11]
test_target = 31
Sol = Solution()
test_solution_list = Sol.combinationSum(test_list, test_target)
print('solution:')
print(test_solution_list)
# test_update_list = Sol.candidate_list_update([], test_list)
# print(test_update_list)
# test_update_list = Sol.candidate_list_update(test_update_list, test_list)
# print(test_update_list)
