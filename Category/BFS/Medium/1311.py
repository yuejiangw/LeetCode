class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        res = defaultdict(int)
        step = 0
        queue = deque([id])
        visited = set()
        visited.add(id)
        while queue and step <= level:
            l = len(queue)
            for _ in range(l):
                curr = queue.popleft()
                if step == level:
                    for video in watchedVideos[curr]:
                        res[video] += 1
                for friend in friends[curr]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            step += 1
        items = list(res.items())
        items.sort(key=lambda x: (x[1], x[0]))
        return [x[0] for x in items]
