from collections import Counter



class Solution:
    def originalDigits(self, s: str) -> str:
        """
        这个题目最有意思的点在于, 你在建立英文单词字典的时候要注意, 必须把含有独一无二字母的单词放前边,
        这样才能保证你每次从哈希表里减去用过的字符时不会把属于别的单词的字母给减掉的.
        这个顺序是: {"zero", "six", "eight", "two", "seven", "five", "four", "three", "one", "nine"}

        时间复杂度: O(N)
        空间复杂度: O(N)
        """
        cnt = Counter(s)
        n0 = cnt.get('z', 0)
        n6 = cnt.get('x', 0)
        n8 = cnt.get('g', 0)
        n2 = cnt.get('w', 0)
        n3 = cnt.get('t', 0) - n2 - n8
        n4 = cnt.get('r', 0) - n3 - n0
        n7 = cnt.get('s', 0) - n6
        n1 = cnt.get('o', 0) - n4 - n2 - n0
        n5 = cnt.get('v', 0) - n7
        n9 = cnt.get('i', 0) - n6 - n8 - n5

        res = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
        return ''.join([str(i) * n for i, n in enumerate(res)])