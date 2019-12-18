'''
Runtime: 60 ms, faster than 73.11% of Python online submissions for Convert BST to Greater Tree.
Memory Usage: 16.2 MB, less than 52.38% of Python online submissions for Convert BST to Greater Tree.
-----------------------------------------------------------------------------------------------------

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

'''




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.currValue = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root and root.right:
            self.convertBST(root.right)
        if root:
            self.currValue += root.val
            root.val = self.currValue
        if root and root.left:
            self.convertBST(root.left)
        return root