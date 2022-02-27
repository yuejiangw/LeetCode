from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # T: O(N)
        # S: O(N)
        counter = defaultdict(int)
        for domain in cpdomains:
            cnt, url = int(domain.split()[0]), domain.split()[1]
            counter[url] += cnt
            url = url.split('.')
            if len(url) == 2:
                parent = url[1]
                counter[parent] += cnt
            elif len(url) == 3:
                parent_1 = url[1] + '.' + url[2]
                parent_2 = url[2]
                counter[parent_1] += cnt
                counter[parent_2] += cnt
        res = []
        for k, v in counter.items():
            res.append(str(v) + ' ' + k)
        return res