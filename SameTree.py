'''
Runtime: 16 ms, faster than 75.17% of Python online submissions for Same Tree.
Memory Usage: 11.9 MB, less than 40.00% of Python online submissions for Same Tree.
-------------------------------------------------------------------------------------
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildList(self, currList, root):
        if root:
            currList.append(root.val)
            self.buildList(currList, root.left)
            self.buildList(currList, root.right)
            return root
        currList.append(0)
        return root

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True

        list1, list2 = [], []
        self.buildList(list1, p)
        self.buildList(list2, q)

        if len(list1) == len(list2):
            for i in range(len(list1)):
                if list1[i] != list2[i]: return False
            return True
        return False

        