def is_balanced(s):
    lower = [0] * 26
    upper = [0] * 26
    word_set = set(list(s))
    for word in word_set:
        if word >= 'a' and word <= 'z':
            idx = ord(word) - ord('a')
            lower[idx] = 1
        else:
            idx = ord(word) - ord('A')
            upper[idx] = 1
    for i in range(26):
        if lower[i] ^ upper[i] == 1:
            return False
    return True

def min_balanced_str(s: str) -> int:
    if not s:
        return -1
    word = set(list(s))
    unbalanced_word = set()
    for w in word:
        if not (w.upper() in word and w.lower() in word):
            unbalanced_word.add(w)
    
    res = []
    for i in range(len(s) - 1):
        if s[i] in unbalanced_word:
            continue
        for j in range(i + 1, len(s)):    
            if s[j] in unbalanced_word:
                break
            if is_balanced(s[i: j + 1]):
                res.append(j - i + 1)
    return -1 if res == [] else min(res)

if __name__ == '__main__':
    test1 = 'azABaabba'
    test2 = 'CATattac'
    print(min_balanced_str(test1))
    print(min_balanced_str(test2))