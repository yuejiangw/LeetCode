def max_num(N: int) -> int:
    s = str(N)
    res = 0
    s = list(s)
    i = 0
    while i < len(s):
        if s[i] == '5':
            del s[i]
            res = max(res, int(''.join(s)))
            s.insert(i, '5')
        i += 1
    return res

if __name__ == '__main__':
    print(max_num(15958))
        