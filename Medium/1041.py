class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        1. 初始方向向上
        2. 一轮指令后，方向可能变也可能不变
        3. 如果方向发生变化，最多四次迭代就能回到初始方向
        4. 第一次回到初始方向之后，查看是否回到了起点
        """
        d = 0   # 0: 上, 1: 右, 2: 下, 3: 左
        x = 0
        y = 0
        while True:
            for i in instructions:
                if i == 'R':
                    d += 1
                elif i == 'L':
                    d -= 1
                else:
                    if d % 4 == 0:
                        y += 1
                    elif d % 4 == 1:
                        x += 1
                    elif d % 4 == 2:
                        y -= 1
                    else:
                        x -= 1
            if d % 4 == 0:
                break
        return (x, y) == (0, 0)
