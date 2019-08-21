class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # all num are positive
        candidates.sort()
        len_candidates = len(candidates)

        _n  = int(target / candidates[0])
        _r = target - _n * candidates[0]

        _solution = []
        if _r == 0:
            for i in range(_n):
                _solution.append(candidates[0])

        for i in range(1, len_candidates):
            if