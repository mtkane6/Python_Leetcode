'''
Runtime: 16 ms, faster than 79.30% of Python online submissions for Univalued Binary Tree.
Memory Usage: 11.6 MB, less than 91.67% of Python online submissions for Univalued Binary Tree.
-----------------------------------------------------------------------------------------------

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def DFS(value, root):
        if not root: return True
        if root.val != value: return False

        if not DFS(value, root.left): return False
        if not DFS(value, root.right): return False
        return True
        
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return None
        value = root.val # the value all nodes must carry for the method to return true.
        return DFS(value, root)