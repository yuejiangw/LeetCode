class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # T: O(3^N), S: O(N)
        res = []
        path = []

        def backtracking(index, value, pre_num):
            if index == len(num):
                if value == target:
                    res.append(''.join(path))
                return
            
            for i in range(index, len(num)):
                curr_str = num[index: i + 1]
                curr_num = int(curr_str)

                # 剪枝 - 如果当前数字前导为 0 则跳过
                if index != i and num[index] == '0':
                    break
                
                if index == 0:
                    # 第一个数字不添加符号
                    path.append(curr_str)
                    backtracking(i + 1, curr_num, curr_num)
                    path.pop()
                else:
                    path.append('+' + curr_str)
                    backtracking(i + 1, value + curr_num, curr_num)
                    path.pop()

                    path.append('-' + curr_str)
                    backtracking(i + 1, value - curr_num, -curr_num)
                    path.pop()

                    path.append('*' + curr_str)
                    backtracking(i + 1, value - pre_num + pre_num * curr_num, pre_num * curr_num)
                    path.pop()
            

        backtracking(0, 0, 0)
        return res