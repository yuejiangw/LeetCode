# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i < j:
            middle = i + (j - i) // 2
            if isBadVersion(middle):
                j = middle
            else:
                i = middle + 1
        return j