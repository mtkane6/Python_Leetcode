'''
Runtime: 12 ms, faster than 91.05% of Python online submissions for Length of Last Word.
Memory Usage: 11.9 MB, less than 46.43% of Python online submissions for Length of Last Word.
----------------------------------------------------------------------------------------------

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        words = list(s.split())
        if len(words) != 0:
            return len(words[len(words)-1])
        else:
            return 0