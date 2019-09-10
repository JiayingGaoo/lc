class Solution:
    def spiralOrder(self, matrix: list) -> list:
        if matrix == []:
            return []
        _index_i = 0
        _index_j = 0
        m_0 = 0
        n_0 = 0
        m_1 = len(matrix)
        n_1 = len(matrix[0])
        if m_1 == 1:
            return matrix[0]
        if n_1 == 1:
            solution_list = []
            for i in range(m_1):
                solution_list.append(matrix[i][0])
            return solution_list
        i_old = 0
        j_old = 0
        solution_list = []
        solution_list.append(matrix[_index_i][_index_j])
        # print(matrix[_index_i][_index_j])
        count = 1
        count_max = m_1 * n_1
        # print(count_max)
        while count < count_max:
            m_0, n_0, m_1, n_1, i_old, j_old, _index_i, _index_j = self.next_indexex(m_0, n_0, m_1, n_1, i_old, j_old,
                                                                                     _index_i, _index_j)
            # print(matrix[_index_i][_index_j])
            # print('output: ', m_0, n_0, m_1, n_1, i_old, j_old, _index_i, _index_j)
            solution_list.append(matrix[_index_i][_index_j])
            count = count + 1
            # print(count, count)
            # print(solution_list)
        return solution_list

    def next_indexex(self, m_0, n_0, m_1, n_1, i_old, j_old, i, j):
        if i == 0 and j == 0:
            return m_0, n_0, m_1, n_1, i, j, i, j + 1

        if i_old == i:
            if j_old < j:
                if j < n_1 - 1:
                    return m_0, n_0, m_1, n_1, i, j, i, j + 1
                if j == n_1 - 1:
                    return m_0, n_0, m_1, n_1, i, j, i + 1, j
            if j_old > j:
                if j > n_0:
                    return m_0, n_0, m_1, n_1, i, j, i, j - 1
                if j == n_0:
                    return m_0, n_0, m_1, n_1, i, j, i - 1, j

        if j_old == j:
            if i_old < i:
                if i < m_1 - 1:
                    return m_0, n_0, m_1, n_1, i, j, i + 1, j
                if i == m_1 - 1:
                    return m_0, n_0, m_1, n_1, i, j, i, j - 1
            if i_old > i:
                if i > (m_0 + 1):
                    return m_0, n_0, m_1, n_1, i, j, i - 1, j
                if i == (m_0 + 1):
                    return m_0 + 1, n_0 + 1, m_1 - 1, n_1 - 1, i, j, i, j + 1


test_matrix = [[ 1, 2, 3, 4, 5],
               [ 6, 7, 8, 9,10],
               [11,12,13,14,15],
               [16,17,18,19,20],
               [21,22,23,24,25]
               ]
Sol = Solution()
test_result = Sol.spiralOrder(test_matrix)
print(test_result)
