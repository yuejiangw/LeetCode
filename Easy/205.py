class Solution:
    '''
    通过hash_map来记录两个字符串中字符的对应关系
    这里需要注意，字符之间必须一一对应
    '''
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = list(s)
        t = list(t)
        hash_map = {}
        for i in range(len(s)):
            # 如果是一个s中新的字符，则需要判断其对应位置的t中的字符
            # 是否已经出现在哈希表中了
            if s[i] not in hash_map.keys():
                if t[i] not in hash_map.values():
                    hash_map[s[i]] = t[i]
                else:
                    return False
            # 如果是一个已经在哈希表中的s中的字符，则需要判断其对应位置的t中的
            # 字符是否与之前对应的字符相同
            else:
                pre_value = hash_map[s[i]]
                if pre_value != t[i]:
                    return False
        return True