class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        _to_str = str(x)
        _to_list = list(_to_str)
        if _to_list[0] == '-':
            return False
        if _to_list[-1] == '0':
            return False
        list_len = len(_to_list)
        for i in range(0, int(list_len/2)):
            if _to_list[i] != _to_list[list_len - 1 - i]:
                return False
        return True


Sol = Solution()
b_palindrome = Sol.isPalindrome(101)
print(b_palindrome)