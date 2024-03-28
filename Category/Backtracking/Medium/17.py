from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letter_map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        path = []
        result = []
        # start_index 代表digits中的第几个字符
        def backtracking(digits, start_index):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
            for i in range(start_index, len(digits)):
                idx = int(digits[i])
                # 对于每一个字符，遍历其对应的letter
                for j in range(len(letter_map[idx])):
                    path.append(letter_map[idx][j])  
                    backtracking(digits, i + 1)
                    path.pop()

        backtracking(digits, 0)
        return result
