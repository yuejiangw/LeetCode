from typing import List

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        child_to_parent = {}
        for region in regions:
            for i in range(1, len(region)):
                child_to_parent[region[i]] = region[0]
        # LCA
        p1, p2 = region1, region2
        while p1 != p2:
            p1 = child_to_parent.get(p1, region1)
            p2 = child_to_parent.get(p2, region2)
        return p1
