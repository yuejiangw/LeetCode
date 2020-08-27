class Solution:
    def list2num(self, l1):
        result = 0
        l = l1[::-1]
        for i in range(len(l)):
            result += l[i] * 10**i 
        return result
    
    def addTwoNumbers(self, l1, l2):
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        result = num1 + num2
        digit_num = len(str(result))
        sum_result = []
        for i in range(digit_num - 1, -1 , -1):
            sum_result.append(result % 10**i)
            result /= 10
        return sum_result

