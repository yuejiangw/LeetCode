class Solution:
    '''
    下标从[0, k]中，偶数下标填充[1,2,3…]，
    奇数下标填充[k + 1, k, k - 1…]，
    后面[k + 1, n - 1]都是顺序填充
    '''
    def constructArray(self, n: int, k: int) -> List[int]:
        i = 0
        num1 = 1
        num2 = k + 1
        result = [0] * n
        while i <= k:
            if i % 2 == 0:
                result[i] = num1
                num1 += 1
            else:
                result[i] = num2
                num2 -= 1
            i += 1
        result[i:] = list(range(k+2, n+1))
        return result
