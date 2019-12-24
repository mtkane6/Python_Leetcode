'''
Runtime: 24 ms, faster than 55.13% of Python online submissions for Height Checker.
Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Height Checker.
------------------------------------------------------------------------------------------

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.

'''


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(i != j for i, j in zip(heights, sorted(heights)))