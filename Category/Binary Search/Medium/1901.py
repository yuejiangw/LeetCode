from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        '''
        对行坐标进行二分，每次比较中间行中的最大值和它上面 / 下面的相邻数字的大小关系
        如果大于它下面的相邻数字，说明要继续在上半部分搜索 right = mid - 1
        如果小于它下面的相邻数字，说明要在下半部分搜索    left = mid + 1

        如果每次二分都是 mat[i] 的最大值比它下面的相邻数字小，那么最后会判断出峰顶行号大于 m-2
        也就是 m-1，因此在初始化时 m-1 不需要在初始二分范围内，并且这样也不用判断越界
        '''
        # T: O(nlogm)，二分 O(logm) 次，每次找当前行的最大值需要 O(n)
        # S: O(1)
        m, n = len(mat), len(mat[0])
        left, right = 0, m - 2
        while left <= right:
            i = (left + right) // 2
            mx = max(mat[i])
            j = mat[i].index(mx)
            if mx > mat[i + 1][j]:
                right = i - 1
            else:
                left = i + 1
        return [left, mat[left].index(max(mat[left]))]