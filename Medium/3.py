"""
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        else:
            max_len = 0
            sub_str = []
            for i in range(len(s)):
                # 到达末尾
                if i == len(s) - 1:
                    break
                else:
                    # 进行字串匹配
                    sub_str.append(s[i])
                    for j in range(i + 1, len(s)):
                        if s[j] in sub_str:
                            max_len = max(max_len, len(sub_str))
                            break
                        else:
                            sub_str.append(s[j])
                max_len = max(max_len, len(sub_str))
                sub_str.clear()

        # max_len = max(max_len, len(sub_str))
        return max(1, max_len)


str1 = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(str1))