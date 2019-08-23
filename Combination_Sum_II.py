class Solution:
    def occur_times(self, candidates: list) -> list:
        len_candidates = len(candidates)
        value_occur_times_in_candidates = []
        for i in range(len_candidates):
            j = 0
            _occur_times = 1
            while j < len_candidates:
                if j != i:
                    if candidates[j] == candidates[i]:
                        _occur_times = _occur_times + 1
                j = j + 1
            value_occur_times_in_candidates.append(_occur_times)
        return value_occur_times_in_candidates

    def combinationSum2(self, candidates: list, target: int) -> list:
        # sort and delete duplications
        candidates.sort()
        # i = 0
        # while i < len(candidates) - 1:
        #     if candidates[i] == candidates[i + 1]:
        #         candidates.pop(i)
        #         i = i - 1
        #     i = i + 1
        len_ori_candidates = len(candidates)
        if len_ori_candidates == 0:
            return []
        if len_ori_candidates == 1:
            if candidates[0] == target:
                return [[candidates[0]]]
            return []
        max_add_number = int(target / candidates[0])
        # print('max_add_number = ',max_add_number)
        # print('candidates:',candidates)
        add_numbers = 1
        solution_list = []
        cur_candidates_list = []
        len_cur_candidate_list = 0
        value_occurs_times_in_ori_candidates_list = self.occur_times(candidates)
        # print('value_occurs_times_in_ori_cnadidate_list:', value_occurs_times_in_ori_candidates_list)
        while add_numbers <= max_add_number:
            cur_candidates_list = self.update_candidates_list(cur_candidates_list, len_cur_candidate_list, candidates,
                                                              len_ori_candidates,
                                                              value_occurs_times_in_ori_candidates_list, target)
            len_cur_candidate_list = len(cur_candidates_list)
            # print('cur_candidates_list:', cur_candidates_list)
            i = 0
            while i < len(cur_candidates_list):
                if cur_candidates_list[i][0] == target:
                    _solution = cur_candidates_list[i][1:]
                    _solution.sort()
                    if _solution not in solution_list:
                        solution_list.append(_solution)
                        # print('find a solution:',_solution)
                        cur_candidates_list.pop(i)
                        len_cur_candidate_list = len_cur_candidate_list - 1
                        continue
                if cur_candidates_list[i][0] > target:
                    cur_candidates_list.pop(i)
                    len_cur_candidate_list = len_cur_candidate_list - 1
                    continue
                i = i + 1
            # print('post_pro, cur_candidate_list:', cur_candidates_list)
            add_numbers = add_numbers + 1
        return solution_list

    def update_candidates_list(self, cur_candidates_list: list, len_cur_candidates_list: int, ori_candidates_list: list,
                               len_ori_candidates_list: int, value_occurs_times_in_ori_candidates_list,
                               target: int) -> list:
        update_candidates_list = []
        if len_cur_candidates_list == 0:
            for i in range(len_ori_candidates_list):
                update_candidates_list.append([ori_candidates_list[i], ori_candidates_list[i]])
            return update_candidates_list

        len_update_candidates_list = 0
        for i in range(len_cur_candidates_list):
            for j in range(len_ori_candidates_list):
                _temp_list = cur_candidates_list[i][0:]
                _occur_times_in_cur_candidates = 0
                for k in range(1, len(cur_candidates_list[i])):
                    if cur_candidates_list[i][k] == ori_candidates_list[j]:
                        _occur_times_in_cur_candidates = _occur_times_in_cur_candidates + 1

                if _occur_times_in_cur_candidates < value_occurs_times_in_ori_candidates_list[j]:
                    _temp_list.append(ori_candidates_list[j])
                    _temp_list[0] = _temp_list[0] + ori_candidates_list[j]
                    if _temp_list[0] <= target:
                        update_candidates_list.append(_temp_list)
                        len_update_candidates_list = len_update_candidates_list + 1
                    else:
                        break

        return update_candidates_list


test_candidates = [10,1,2,7,6,1,5]
test_target = 8
Sol = Solution()
test_solution_list = Sol.combinationSum2(test_candidates, test_target)
print(test_solution_list)