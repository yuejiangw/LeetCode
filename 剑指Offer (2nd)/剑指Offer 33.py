class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def judge(postorder):
            if len(postorder) == 0:
                return True

            # root value
            root = postorder[-1]
            
            # left subtree of the root
            i = 0
            while i < len(postorder) - 1 and postorder[i] < root:
                i += 1
            left_tree = postorder[: i]

            # right subtree of the root
            j = i
            while j < len(postorder) - 1 and postorder[j] > root:
                j += 1
            if j != len(postorder) - 1:
                return False
            right_tree = postorder[i: j]

            return judge(left_tree) and judge(right_tree)
        
        return judge(postorder)