class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 列出所有可能的子数组长度
        length = list(range(1, len(arr) + 1, 2))

        # 通过切片获取所有子数组
        subArrays = []
        for l in length:
            i = 0
            while i + l <= len(arr):
                subArrays.append(arr[i:i + l])
                i += 1
                
        # 累加结果
        result = 0
        for a in subArrays:
            result += sum(a)
        return result