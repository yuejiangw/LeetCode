class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        
        # 贪心，h按照从高到低的顺序排序，k按从低到高排序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        result = []
        for p in people:
            # 如果前面不能有更高的人，则直接插入到头部
            if p[1] == 0:
                result.insert(0, p)
            # 如果前面有k个比他高的人，则插入到第k位
            else:
                result.insert(p[1], p)
        return result