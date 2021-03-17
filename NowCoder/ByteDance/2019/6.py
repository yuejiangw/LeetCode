'''字节跳动2019春招研发
找零
Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，
以及面值1024元的纸币。现在小Y使用1024元的纸币购买了一件价值为的商品，
请问最少他会收到多少硬币？
@ Input:
一行，包含一个数N。

@ Output:
一行，包含一个数，表示最少收到的硬币数。

@ Sample Input:
200

@ Sample Output:
17
'''
N = 1024 - int(input())
coins = [64, 16, 4, 1]
num = 0
for c in coins:
    num += N // c
    N = N % c
print(num)