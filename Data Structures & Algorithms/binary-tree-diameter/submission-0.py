# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # helper dfs returns height
        def dfs(curr):
            if not curr: # leaf node returns 0
                return 0
            left = dfs(curr.left) # get left height
            right = dfs(curr.right) # get right height
        
            self.res = max(self.res, left + right) # result is the max between what we already have found and what we currently are at
            return 1 + max(left, right) # return max height + 1
        dfs(root) # run it
        return self.res # return the max we found

        