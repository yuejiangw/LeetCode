from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """拓扑排序
        将 recipes 中的菜也看做是 ingredient 的一员, 每个 ingredient 看做图中的一个节点
        根据 ingredient 和 recipe 之间的关系建立依赖图并记录每个 recipe 的入度
        之后进行拓扑排序
        """
        # 假设 len(recipes) = n, d 是每一个 recipe 的最大长度, len(supplies) = m
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
                for recipe in graph[curr]:
                    count[recipe] -= 1
                    if count[recipe] == 0:
                        queue.append(recipe)
                        res.append(recipe)
        return res


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # 另一种解法，直接从 recipe 出发
        # 入度表只用作初始化，之后的 BFS 扩展使用了 set 的性质
        # 和第一种解法的区别主要在于建图，第一个解法的图是从 ingredient 指向 recipe，本解法的图是从 recipe 指向 ingredient
        supplies = set(supplies)
        indegree = {}
        graph = {}

        for i in range(len(recipes)):
            recipe, ingredient = recipes[i], ingredients[i]
            indegree[recipe], graph[recipe] = 0, set()
            for ing in ingredient:
                # 对于当前 recipe 所需的所有 ingredient，只有当它不属于初始 ingredient 的时候才将其加入 graph
                if ing not in supplies:
                    indegree[recipe] += 1
                    graph[recipe].add(ing)
        
        queue = deque()
        visited = set()
        for recipe, count in indegree.items():
            if count == 0:
                queue.append(recipe)
                visited.add(recipe)
        
        res = []
        while queue:
            recipe = queue.popleft()
            res.append(recipe)
            supplies.add(recipe)
            for r in graph:
                if graph[r] < supplies and r not in visited:
                    queue.append(r)
                    visited.add(r)
        return res
