from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        对角线元素的特点是，它的坐标 (i, j)，其所在的对角线编号为 i + j
        同一对角线的元素，需要按照列索引的逆序依次输出
        T: O(N), S: O(N)
        '''
        diagonal_map = defaultdict(list)
        
        # 所有元素存入对角线
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                diagonal_map[i + j].append(nums[i][j])
        
        # 依次将所有对角线元素按顺序拼接
        res = []
        curr = 0
        while curr in diagonal_map:
            res.extend(diagonal_map[curr])
            curr += 1
        
        return res