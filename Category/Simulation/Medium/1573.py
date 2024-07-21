class Solution:
    def numWays(self, s: str) -> int:
        '''
        把 s 分成三部分，需要两个挡板，一共可选的空位是 n - 1 个，分情况讨论：
        1. 如果 s 中 1 的个数不是 3 的倍数，直接返回 0
        2. s 中 1 的个数是 3 的倍数，每组应该有 count / 3 个 1，
        3. 特殊情况：s 全是 0，则答案是 C n-1 2 = (n-1) * (n-2) / 2
        '''
        n = len(s)
        res = 0
        count_of_1 = s.count('1')
        
        if count_of_1 == 0:
            res = (n - 1) * (n - 2) // 2 
        elif count_of_1 % 3 != 0:
            res = 0
        elif count_of_1 % 3 == 0:
            target = count_of_1 // 3
            count = 0
            cut1_choice, cut2_choice = 0, 0
            i = 0
            while i < len(s):
                c = s[i]
                i += 1
                if c == '1':
                    count += 1
                    if count == target:
                        # find cut_1 position
                        cut1_choice = 1
                        # find number of zeros between the cut1 position and the first one after it
                        while i < len(s) and s[i] == '0':
                            cut1_choice += 1
                            i += 1
                    elif count == 2 * target:
                        # find cut_2 position
                        cut2_choice = 1
                        # find number of zeros between the cut2 position and the first one after it
                        while i < len(s) and s[i] == '0':
                            cut2_choice += 1
                            i += 1
            res = cut1_choice * cut2_choice

        return res % (10**9 + 7)