class Solution:
    def sortSentence(self, s: str) -> str:
        """ 最后一个数字当做数组下标, O(N) """
        s = s.strip().split()
        res = [''] * len(s)
        for word in s:
            idx = int(word[-1]) - 1
            res[idx] = word[:-1]
        return ' '.join(res)


    def sortSentence(self, s: str) -> str:
        """ 排序, O(NlogN) """
        s = s.strip().split()
        return ' '.join([x[:-1] for x in sorted(s, key=lambda x: x[-1])])