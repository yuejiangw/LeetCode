from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """拓扑排序
        将 recipes 中的菜也看做是 ingredient 的一员, 每个 ingredient 看做图中的一个节点
        根据 ingredient 和 recipy 之间的关系建立依赖图并记录每个 recipy 的入度
        之后进行拓扑排序
        """
        # 假设 len(recipies) = n, d 是每一个 recipy 的最大长度, len(supplies) = m
        # T: O(dn + m)
        # S: O(dn + m)
        n = len(recipes)
        res = []
        count = defaultdict(int)
        graph = defaultdict(list)
        for i in range(n):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
            count[recipes[i]] = len(ingredients[i])
        
        queue = deque(supplies)
        
        while queue:
            curr = queue.popleft()
            if curr in graph:
                for recipy in graph[curr]:
                    count[recipy] -= 1
                    if count[recipy] == 0:
                        queue.append(recipy)
                        res.append(recipy)
        return res

