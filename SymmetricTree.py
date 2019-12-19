'''
Runtime: 20 ms, faster than 77.49% of Python online submissions for Symmetric Tree.
Memory Usage: 12 MB, less than 63.04% of Python online submissions for Symmetric Tree.
------------------------------------------------------------------------------------------

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def buildLeftList(self, currList, root):
        if root:
            currList.append(root.val)
            self.buildLeftList(currList, root.left)
            self.buildLeftList(currList, root.right)
            return root
        currList.append(0)
        return root
    def buildRightList(self, currList, root):
        if root:
            currList.append(root.val)
            self.buildRightList(currList, root.right)
            self.buildRightList(currList, root.left)
            return root
        currList.append(0)
        return root


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if not root.left and not root.right: return True
        if not root.right or not root.left: return False

        leftList, rightList = [], []
        self.buildLeftList(leftList, root.left)
        self.buildRightList(rightList, root.right)

        if len(leftList) == len(rightList):
            for i in range(len(leftList)):
                if leftList[i] != rightList[i]: return False
            return True
        return False