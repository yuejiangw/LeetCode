class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers[0] + numbers[1] > target:
            return []

        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
                
        return []