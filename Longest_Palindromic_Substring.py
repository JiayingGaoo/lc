class Solution:
    def is_palindrome(self, s: str) -> bool:
        len_str = len(s)
        if len_str == 1:
            return True
        for i in range(0, int(len_str/2)):
            if s[i] != s[len_str - 1 - i]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        len_str = len(s)
        if len_str == 0:
            return ''
        if len_str == 1:
            return s

        padding = len_str
        while padding > 0:
            for i in range(0, len_str - 1):
                end_id = i + padding - 1
                if end_id < len_str:
                    if s[i] == s[end_id]:
                        temp_str = s[i:end_id + 1]
                        # temp_str = ''
                        # for j in range(i, end_id + 1):
                        #     temp_str = temp_str + s[j]
                        # obtain the temp_str under given i and padding
                        if self.is_palindrome(temp_str):
                            return temp_str
                else:
                    break
            padding = padding - 1
        return s[0]

    def longestPalindrome_1(self, s: str) -> str:
        len_str = len(s)
        if len_str == 0:
            return ''
        if len_str == 1:
            return s
        cur_max_len_palindrome = 1
        cur_best_palindrome = s[0]
        for i in range(0, len_str):
            remain_max_len = len_str - i
            # print(remain_max_len)
            if remain_max_len > cur_max_len_palindrome:
                for j in range(len_str - 1, i, -1):
                    len_temp_str = j - i + 1
                    if len_temp_str > cur_max_len_palindrome:
                        if s[i] == s[j]:
                            temp_str = ''
                            for k in range(i, j + 1):
                                temp_str = temp_str + s[k]
                            if self.is_palindrome(temp_str):
                                cur_max_len_palindrome = len_temp_str
                                cur_best_palindrome = temp_str
                                print(cur_best_palindrome, cur_max_len_palindrome)
                                break
                    else:
                        break
            else:
                return cur_best_palindrome
        return cur_best_palindrome

test_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# test_str = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
# print('the length of test_str is: ', len(test_str))
Sol = Solution()
test_output_palindrome = Sol.longestPalindrome(test_str)
print(test_output_palindrome)