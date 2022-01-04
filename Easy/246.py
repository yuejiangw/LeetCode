class Solution:
    """ 遍历，时间复杂度O(n) """
    def isStrobogrammatic(self, num: str) -> bool:
        hash_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res = ""
        for n in num:
            if n in hash_map:
                res += hash_map[n]
            else:
                return False
        return res[::-1] == num


class Solution:
    """ 二分，时间复杂度O(logn) """
    def isStrobogrammatic(self, num: str) -> bool:
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] == num[j]:
                if num[i] in {'0', '1', '8'}:
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                if (num[i] == '6' and num[j] == '9') or\
                        (num[i] == '9' and num[j] == '6'):
                    i += 1
                    j -= 1
                else:
                    return False
        return True
