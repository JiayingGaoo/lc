class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # do not use find function
        if needle == '':
            return 0
        for i in range(0, len(haystack) - len(needle)):
            if haystack[i] == needle[0]:
                be_a_part = True
                for j in range(1, len(needle)):
                    if needle[j] != haystack[i + j]:
                        be_a_part = False
                        break
                if be_a_part:
                    return i
        return -1

Sol = Solution()
print(Sol.strStr('hello', 'll'))