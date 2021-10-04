## Better公司的OA试题

1. 第一题就是给你两个input分别是d和k，让你返回从d开始、经过了k天之后是星期几。比如input是“星期一”和6那就返回“星期天”；input是“星期六”和3就返回“星期二”以此类推

2. 第二题大概是这样的，他定义了一种叫balancedstring的东西，也就是说当一个string的所有出现过的字母都出现了大小写这个string就是balanced反之就不是。比如"Aba"就不是balanced，因为"Aba"里面出现了小写的b却没有大写的B但是"AbaB""AAbaB""bBaBAcC"都是balanced。题目的input是一个string，你的任务是返回一个最小的substring的length where this substring是balanced

3. 第三题就是给你一个数字，你需要从这个数字里去掉一个5，让你返回所有去掉5之后可能产生的数字中最大的数字。比如input是15958，你就有两种去掉5的方法分别得到1958和1598。我们要返回1958因为1958 > 1598

## 解法思路

1. 使用哈希表记录星期与下标的对应关系，新的下标为(原下标 + k) % 7 
   
2. 暴力 + 剪枝
   
3. 字符串转整数，暴力解