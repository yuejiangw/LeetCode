class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return 0 if needle == "" else haystack.find(needle)

class Solution:
    """暴力解法，并利用短路表达式简单地优化了一下"""
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if not needle:
            return 0
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i: i + length] == needle:
                return i
        return -1