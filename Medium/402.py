class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """ 单调递增栈 """
        stack = []
        for d in num:
            # 如果当前访问的数字比栈顶数字小，那么应该不断将栈顶数字出栈
            # 直到栈顶数字小于等于当前访问数字，并将 k 的值减一，代表已经移除了一个元素
            # 当k的值为0的时候不应该做任何出栈操作，因为已经达到了可移除字符数量的最大限制
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        # 如果最终 k 的值大于0，说明我们还剩 k 个字符没有移除
        # 因此我们应该舍去末尾的 k 个字符
        if k > 0:
            stack = stack[:-k]
        # 可能有 ’0‘ 出现在栈的头部，因此要使用 lstrip(’0‘) 去除
        return ''.join(stack).lstrip('0') or '0'
