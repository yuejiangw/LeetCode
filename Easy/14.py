# 利用python的max()和min()，在Python里字符串是可以比较的，
# 按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
# 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
            