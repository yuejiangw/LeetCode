from collections import deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """双向 BFS
        使用两个队列 lqueue 和 rqueue
        时间复杂度和空间复杂度与普通 BFS 一样, 但可以极大地减少搜索空间, 提升速度
        """
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)
        lvisited = set()
        rvisited = set()
        lqueue = deque()
        rqueue = deque()
        
        lqueue.append(beginWord)
        rqueue.append(endWord)

        lvisited.add(beginWord)
        rvisited.add(endWord)
        step = 0

        while lqueue and rqueue:
            # 为了保证搜索的平衡性, 如果 lqueue 的长度较大, 则立刻交换 lqueue 和 rqueue
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            step += 1
            for k in range(len(lqueue)):
                # 如果当前的单词已经出现在另一个方向 bfs 的搜索空间中, 说明找到一条路径
                cur = lqueue.popleft()
                if cur in rvisited:
                    return step
                
                for i in range(m):        
                    for j in range(26):
                        tmp = cur[:i] + chr(97+j) + cur[i+1:]
                        if tmp not in lvisited and tmp in st:
                            lqueue.append(tmp)
                            lvisited.add(tmp)
                       
        return 0
