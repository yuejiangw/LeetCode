class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        每个非空的二叉树节点都会产生两条边，消耗一条边，而每个空节点只会消耗一条边
        根节点只会产生两条边而不会消耗，因此 edge 数量初始化为1
        """
        edge = 1
        for node in preorder.split(','):
            if node == '#':
                edge -= 1
                # 任何情况下 edge 数量都应该大于0
                if edge < 0:
                    return False
            else:
                edge -= 1
                if edge < 0:
                    return False
                edge += 2
        return edge == 0
