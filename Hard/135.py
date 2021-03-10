class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 初始化
        result = [1] * len(ratings)
        
        # 从左往右遍历，如果右边孩子评分比相邻的左边孩子评分高，
        # 则右边孩子的糖果数更新为左边孩子的糖果数+1
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                result[i+1] = result[i] + 1
        
        # 从右往左遍历，如果左边的孩子评分比相邻的右边孩子评分高，
        # 而且左边孩子的糖果数量不大于右边孩子的糖果数量（因为要求总数最少），
        # 则左边孩子的糖果数为右边孩子的糖果数+1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i] and result[i-1] <= result[i]:
                result[i-1] = result[i] + 1
        
        return sum(result)