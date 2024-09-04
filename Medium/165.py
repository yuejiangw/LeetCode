class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 更简洁的写法
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        n = max(len(version1), len(version2))

        for i in range(n):
            s1 = version1[i] if i < len(version1) else '0'
            s2 = version2[i] if i < len(version2) else '0'
            if int(s1) < int(s2):
                return -1
            elif int(s1) > int(s2):
                return 1
        return 0


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if int(v1[i]) < int(v2[j]):
                return -1
            elif int(v1[i]) > int(v2[j]):
                return 1
            else:
                i += 1
                j += 1
        
        while i < len(v1):
            if int(v1[i]) != 0:
                return 1
            i += 1
        while j < len(v2):
            if int(v2[j]) != 0:
                return -1
            j += 1
        return 0