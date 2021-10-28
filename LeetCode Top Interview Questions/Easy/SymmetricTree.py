'''
LeetCode 101. Symmetric Tree
Language : Python
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

    # 1. Recursively
    #     else:
    #         return self.check(root.left, root.right)
    #
    # def check(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     if left is None or right is None:
    #         return False
    #     if left.val == right.val:
    #         aPair = self.check(left.left, right.right)
    #         bPair = self.check(left.right, right.left)
    #         return aPair and bPair
    #     else:
    #         return False
    # 2. Iteratively
        stack = [[root.left, root.right]]

        while stack:
            pair = stack.pop()
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False

        return True
