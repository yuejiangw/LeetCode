from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, email):
        # 查找根节点 + 路径压缩
        if self.parent[email] != email:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, email1, email2):
        r1, r2 = self.find(email1), self.find(email2)
        if r1 != r2:
            self.parent[r2] = r1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        
        # 初始化每个邮箱的 parent 指向自己
        for account in accounts:
            for email in account[1:]:
                if email not in uf.parent:
                    uf.parent[email] = email
        
        # 合并同一账户的邮箱
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                uf.union(first_email, email)
        
        # 根据邮箱根节点归类所有邮箱
        email_to_name = {}
        email_groups = defaultdict(list)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                root = uf.find(email)
                email_groups[root].append(email)
        
        # 收集结果
        res = []
        for root, emails in email_groups.items():
            unique_emails = sorted(set(emails))
            res.append([email_to_name[root]] + unique_emails)
        return res