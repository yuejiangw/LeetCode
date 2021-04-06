class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        # 计数
        hash_map = {}
        for x in s:
            if x in hash_map.keys():
                hash_map[x] += 1
            else:
                hash_map[x] = 1
        # 按照value从大到小排序
        hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        # 输出
        result = []
        for item in hash_map:
            result += item[0] * item[1]
        return ''.join(result)
        