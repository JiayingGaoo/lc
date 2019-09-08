class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0
        if len_s == 1:
            if s[0] == ' ':
                return 0
            return 1
        # find the last word:
        end_id = len_s - 1
        if s[len_s - 1] == ' ':
            find_end_id = False
            for i in range(len_s-1, 0, -1):
                if s[i] == ' ' and s[i - 1] != ' ':
                    find_end_id = True
                    end_id = i - 1
                    break
            if not find_end_id:
                return 0
        # print('end_id =', end_id)
        # start_id
        start_id = 0
        for i in range(end_id, 0, -1):
            # some case can determine the start_id
            if s[i] != ' ' and s[i-1] == ' ':
                start_id = i
                break
        # print('start_id =', start_id)
        return end_id - start_id + 1


test_str = "        "
Sol = Solution()
test_result = Sol.lengthOfLastWord(test_str)
print(test_result)

