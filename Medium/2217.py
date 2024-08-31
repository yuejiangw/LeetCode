from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        '''
        脑筋急转弯，长度为intLength的第x个回文数是多少？
        [1000][001]为长度为7的第一个回文数，那么第376个回文数为[1375][731]
        只需要看左半部分即可, 右半部分可以通过对称性推出
        '''
        def getAns(base, query):
            # 最多可以有的回文数是 9 * base 个
            max_num = 9 * base
            if query > max_num:
                return -1
            # base + query - 1 就是第 query 大的回文串的左半部分
            left_part = base + query - 1
            if intLength % 2 == 0:
                # 如果 intLength 是偶数，则直接把 left_part 对称复制即可
                return int(str(left_part) + str(left_part)[::-1])
            else:
                # 如果 intLength 是奇数，则把 left_part除了最后一个字符以外的子串对称复制，即 left_part[0:-1]
                return int(str(left_part) + str(left_part)[0:-1][::-1])

        base = pow(10, (intLength - 1) // 2)
        res = []
        for q in queries:
            res.append(getAns(base, q))
        return res
