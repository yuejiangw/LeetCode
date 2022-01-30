from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # 遍历每行，把石头搬到尽可能远的位置 (move_pos)，然后旋转
        for row in box:
            move_pos = len(row) - 1
            for col in range(len(row) - 1, -1, -1):
                if row[col] == '*':
                    move_pos = col - 1
                elif row[col] == '#':
                    row[col], row[move_pos] = row[move_pos], row[col]
                    move_pos -= 1
        return [list(x[::-1]) for x in zip(*box)]
