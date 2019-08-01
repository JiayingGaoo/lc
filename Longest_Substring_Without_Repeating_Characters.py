class Solution:
    def without_repeating(self, s: str)-> bool:
        len_str = len(s)
        for i in range(0, len_str):
            for j in range(i + 1, len_str):
                if s[j] == s[i]:
                    return False
        return True


    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the start char index in s one after another, and check the possible substrings
        len_str = len(s)
        cur_max_substring_len = 0
        for start_id in range(0, len_str):
            temp_str = ''
            for _s_id in range(start_id, len_str):
                temp_str = temp_str + s[_s_id]
                # judge whether temp_str is satisfied the requirment
                cur_temp_str_len = len(temp_str)
                if cur_temp_str_len > cur_max_substring_len:
                    if self.without_repeating(temp_str):
                        cur_max_substring_len = cur_temp_str_len
                        print(temp_str, cur_max_substring_len)
                    else:
                        break

        return cur_max_substring_len

test_str = "pwwkew"
Sol = Solution()
Sol.lengthOfLongestSubstring(test_str)