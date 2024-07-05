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