from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [transaction.split(',') for transaction in transactions]
        # 按照名字进行排序，是为了将同一个人的所有transaction连在一起
        transactions = sorted(transactions, key=lambda x: x[0])

        res = []
        idx = set()  # idx用来记录已经访问过的下标，防止将某些transaction重复写入res
        for i in range(len(transactions)):
            t1 = transactions[i]
            # 如果单笔金额大于1000且未被记录过，则插入res
            if int(t1[2]) > 1000:
                if i not in idx:
                    res.append(','.join(t1))
                    idx.add(i)

            j = i + 1
            while j < len(transactions) and transactions[j][0] == t1[0]:
                t2 = transactions[j]
                # 如果同一个人的连续两笔交易时间间隔 ≤ 60，且位于不同的城市，且未被记录过，则插入res
                if abs(int(t1[1]) - int(t2[1])) <= 60 and t1[3] != t2[3]:
                    if i not in idx:
                        res.append(','.join(t1))
                        idx.add(i)
                    if j not in idx:
                        res.append(','.join(t2))
                        idx.add(j)
                j += 1
        return res

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [t.split(',') for t in transactions]
        res = []
        for i in range(len(transactions)):
            name, time, amount, city = trans[i]
            # total amount invalid
            if int(amount) > 1000:
                res.append(transactions[i])
                continue
            # check from the beginning of the transactions to see if there is time invalid
            for j in range(len(transactions)):
                if i == j:
                    continue
                n, t, a, c = trans[j]
                if n == name and abs(int(t) - int(time)) <= 60 and city != c:
                    res.append(transactions[i])
                    break
        return res