"""
input: d, k
return: 从 d 开始经过了 k 天是星期几
eample: 
    d = "Saturday", k = 3
    return = "Tuesday"

    d = "Monday", k = 6
    return = "Sunday"
idea: hashmap + mod
"""
def solution(d: str, k: int) -> str:
    week = {'Mon': 0, 'Tue': 1, 'Wed': 2,
            'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    reverse_week = {v:k for k, v in week.items()}
    return reverse_week[(week[d] + k) % 7]

if __name__ == '__main__':
    print(solution('Sat', 3))
    print(solution('Mon', 6))