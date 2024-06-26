class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        i, j = 0, 0
        while i < len(version1) and j < len(version2):
            curr_v1 = int(version1[i])
            curr_v2 = int(version2[j])
            if curr_v1 > curr_v2:
                return 1
            elif curr_v1 < curr_v2:
                return -1
            else:
                i += 1
                j += 1
        
        if i == len(version1) and j == len(version2):
            return 0

        while i == len(version1) and j < len(version2):
            curr_v2 = int(version2[j])
            if curr_v2 > 0:
                return -1
            j += 1
        
        while i < len(version1) and j == len(version2):
            curr_v1 = int(version1[i])
            if curr_v1 > 0:
                return 1
            i += 1
        
        return 0
