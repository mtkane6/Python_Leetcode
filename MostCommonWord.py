'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
'''
import string

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        words = list(paragraph.split())
        # remove any punctuation like ,."')
        words = [item.strip(string.punctuation) for item in words]

        wordDict = {}
        for i in words:
            if i in wordDict.keys():
                wordDict[i.lower()] += 1
            else:
                wordDict[i.lower()] = 0

        for i in range(len(wordDict)):
            _,highestCountWord = max(zip(wordDict.values(),wordDict.keys()))
            if highestCountWord in banned:
                del wordDict[highestCountWord]
                continue
            else:
                return highestCountWord
        return None
        
