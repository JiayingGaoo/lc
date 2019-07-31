class Solution:
    def romanToInt(self, s: str) -> int:
        # divide the s into several parts
        s_pro = []
        s_remain = list(s)
        while len(s_remain) > 0:
            # print the current s_remain
            # update s_remain_str by the current s_remain
            s_remain_str = ''
            for _s in s_remain:
                s_remain_str = s_remain_str + _s
            print('cur_s_remain_str: ', s_remain_str)

            # the case for two letters: IV, IX, XL, XC, CD and CM
            # IV
            i_find = s_remain_str.find('IV')
            if i_find >= 0:
                s_pro.append(4)
                s_remain.pop(i_find)
                s_remain.pop(i_find)
                continue
            # IX
            i_find = s_remain_str.find('IX')
            if i_find >= 0:
                s_pro.append(9)
                s_remain.pop(i_find)
                s_remain.pop(i_find)
                continue
            # XL
            i_find = s_remain_str.find('XL')
            if i_find >= 0:
                s_pro.append(40)
                s_remain.pop(i_find)
                s_remain.pop(i_find)
                continue
            # XC
            i_find = s_remain_str.find('XC')
            if i_find >= 0:
                s_pro.append(90)
                s_remain.pop(i_find)
                s_remain.pop(i_find)
                continue
            # CD
            i_find = s_remain_str.find('CD')
            if i_find >= 0:
                s_pro.append(400)
                s_remain.pop(i_find)
                s_remain.pop(i_find)
                continue
            # CM
            i_find = s_remain_str.find('CM')
            if i_find >= 0:
                s_pro.append(900)
                s_remain.pop(i_find)
                s_remain.pop(i_find)
                continue

            # The case for single letter
            # I
            i_find = s_remain_str.find('I')
            if i_find >= 0:
                s_pro.append(1)
                s_remain.pop(i_find)
                continue
            # V
            i_find = s_remain_str.find('V')
            if i_find >= 0:
                s_pro.append(5)
                s_remain.pop(i_find)
                continue
            # X
            i_find = s_remain_str.find('X')
            if i_find >= 0:
                s_pro.append(10)
                s_remain.pop(i_find)
                continue
            # L
            i_find = s_remain_str.find('L')
            if i_find >= 0:
                s_pro.append(50)
                s_remain.pop(i_find)
                continue
            # C
            i_find = s_remain_str.find('C')
            if i_find >= 0:
                s_pro.append(100)
                s_remain.pop(i_find)
                continue
            # D
            i_find = s_remain_str.find('D')
            if i_find >= 0:
                s_pro.append(500)
                s_remain.pop(i_find)
                continue
            # M
            i_find = s_remain_str.find('M')
            if i_find >= 0:
                s_pro.append(1000)
                s_remain.pop(i_find)
                continue
        # print(s_pro)
        return sum(s_pro)


Sol = Solution()
test_roman_str = "MCMXCVI"
i = Sol.romanToInt(test_roman_str)
print(i)