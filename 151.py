"""
    题目描述：给定一个字符串，逐个翻转字符串中的每个单词。
    无空格字符构成一个单词。
    输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

class Solution():
    def reverseWords(self, str):
        str2list = str.strip().split(' ')
        result = []
        for word in str2list:
            if word != '':
                result.append(word)
        return ' '.join(result[::-1])


str1 = "the sky is blue"
str2 = "  hello world!  "
str3 = "a good    example"

solution = Solution()
result1 = solution.reverseWords(str1)
result2 = solution.reverseWords(str2)
result3 = solution.reverseWords(str3)
print(result1 + '\n' + result2 + '\n' + result3)