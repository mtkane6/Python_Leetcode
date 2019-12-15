'''
Runtime: 32 ms, faster than 90.92% of Python online submissions for Two Sum.
Memory Usage: 13.1 MB, less than 39.04% of Python online submissions for Two Sum.


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in numsMap:
                solution = [numsMap[value], i]
                return solution
            else:
                numsMap[nums[i]] = i
        return 0


    print(twoSum([2,7, 11, 15],9))