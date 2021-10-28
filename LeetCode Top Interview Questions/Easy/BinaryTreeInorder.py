'''
LeetCode 94. Binary Tree Inorder Traversal
Language : Python
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. DFS
        if root is None:
            return []

        answer = []

        def inorder(node):
            if node:
                inorder(node.left)
                answer.append(node.val)
                inorder(node.right)

        inorder(root)
        # 2. Iteratively
        # stack = [root]
        # answer = []
        #
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         stack.append(node.right)
        #         stack.append(node)
        #         stack.append(node.left)
        #     else:
        #         if stack:
        #             node = stack.pop()
        #             answer.append(node.val)
        #
        return answer
