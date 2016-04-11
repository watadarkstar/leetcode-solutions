"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

TODO: this was easy more or less but can be cleaned up
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if root == None:
                return 0, True
            
            left = depth(root.left)
            right = depth(root.right)
            
            balanced = left[1] and right[1]
            if balanced:
                balanced = abs(left[0] - right[0]) <= 1
            
            return 1 + max(left[0], right[0]), balanced
        
        return depth(root)[1]
