'''
LeetCode 104. Maximum Depth of Binary Tree
Language : Python
'''

from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    # 1. Iteratively
        tmp = deque([root])
        depth = 0

        while tmp:
            for _ in range(len(tmp)):
                node = tmp.popleft()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            depth += 1

        return depth
    # 2. Recursively
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1