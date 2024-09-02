from typing import List
from collections import *

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        most_popular = float('-inf')
        hashmap = {}
        res = []

        for (creator, vid, view) in zip(creators, ids, views):
            if creator not in hashmap:
                hashmap[creator] = [view, view, vid] # [total_view, curr_max_view, max_view_vid]
            else:
                info = hashmap[creator]
                info[0] += view
                if view > info[1]:
                    info[1] = view
                    info[2] = vid
                elif view == info[1]:
                    info[2] = min(info[2], vid)
            
            most_popular = max(most_popular, hashmap[creator][0])
        
        res = []
        for k, v in hashmap.items():
            if v[0] == most_popular:
                res.append([k, v[2]])
        return res

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        most_viewed_videos = defaultdict(deque)
        max_view = defaultdict(int)
        popularity = defaultdict(int)

        max_popularity = float('-inf')
        popular_creator = set()

        for i in range(len(creators)):
            creator, vid, view = creators[i], ids[i], views[i]
            popularity[creator] += view
            if view >= max_view[creator]:
                if view > max_view[creator]:
                    max_view[creator] = view
                    most_viewed_videos[creator].clear()
                if len(most_viewed_videos[creator]) == 0 or most_viewed_videos[creator][0] <= vid:
                    most_viewed_videos[creator].append(vid)
                else:
                    most_viewed_videos[creator].appendleft(vid)

            if popularity[creator] > max_popularity:
                popular_creator.clear()
                popular_creator.add(creator)
                max_popularity = popularity[creator]
            elif popularity[creator] == max_popularity:
                popular_creator.add(creator)
        
        res = []
        for creator in popular_creator:
            res.append([creator, most_viewed_videos[creator][0]])
        return res
