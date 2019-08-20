class Solution:
    def isValidSudoku(self, board: list) -> bool:
        _only_contain_digits_and_dots = self.only_contain_digits_and_dots(board)
        if not _only_contain_digits_and_dots:
            return False

        # every row
        for i in range(0, 9):
            _without_repetition = self.a_block_without_repetition(board[i])
            if not _without_repetition:
                return False

        # every column
        for j in range(0, 9):
            _column = []
            for i in range(0, 9):
                _column.append(board[i][j])
            _without_repetition = self.a_block_without_repetition(_column)
            if not _without_repetition:
                return False

        # every 9
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                _block = [board[i-1][j-1], board[i-1][j], board[i-1][j+1], board[i][j-1], board[i][j], board[i][j+1], board[i+1][j-1], board[i+1][j], board[i+1][j+1]]
                _without_repetition = self.a_block_without_repetition(_block)
                if not _without_repetition:
                    return False
        return True

    def a_block_without_repetition(self, block: list) -> bool:
        for _cur_id in range(0, 9):
            for i in range(_cur_id+1, 9):
                if block[i] == block[_cur_id] and block[_cur_id] != '.':
                    return False
        return True

    def only_contain_digits_and_dots(self, board: list) -> bool:
        for _board in board:
            for _b in _board:
                if _b not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                    return False
        return True


test_str = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
Sol = Solution()
test_result = Sol.isValidSudoku(test_str)
print(test_result)
