# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = '|'
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                res += str(curr.val) + '|'
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res += '#|'
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split('|')[1: -1]
        nodes = []
        for d in data:
            if d == '#':
                nodes.append(None)
            else:
                nodes.append(TreeNode(int(d)))
        
        root = nodes[0]
        i = 0
        null_num = 0
        while 2 * (i - null_num) + 2 < len(nodes):
            if not nodes[i]:
                null_num += 1
            else:
                nodes[i].left = nodes[2 * (i - null_num) + 1]
                nodes[i].right = nodes[2 * (i - null_num) + 2]
            i += 1
        return root 
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))