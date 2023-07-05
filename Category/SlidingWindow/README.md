# 滑动窗口算法

## 算法思想概述

本质上是双指针算法，两个指针一左一右维护一个窗口的两个边界，通过分别控制两个指针移动来控制窗口的扩张或收缩，从而能够在 O(N) 的时间复杂度内实现对整个字符串 or 数组的动态扫描

## 适用题型 + 技巧

* 最长 + 连续，有了这两个条件一般都可以用滑动窗口
* 一般搭配 Set 或 Map 使用，从而判断窗口内是否出现重复元素

## 模板

```python
import defaultdict from collecitons

# 假设我们有一个字符串 s
i, j = 0, 0
window = defaultdict(int)
res = 0
while j < len(s):
    # 记录当前右边界字符
    c = s[j]
    # 右边界扩大
    j += 1
    # 更新窗口信息
    window[c] += 1
    # 检查左边界是否需要收缩
    while window[c] > 1:
        d = s[i]
        i += 1
        window[d] -= 1
    
    # 当窗口停止收缩时，代表当前找到了一个可能满足条件的连续子串 or 子数组
    # 判断是否可以更新结果值
    res = max(res, j - i)
```