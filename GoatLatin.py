'''
Runtime: 16 ms, faster than 78.21% of Python online submissions for Goat Latin.
Memory Usage: 11.7 MB, less than 73.33% of Python online submissions for Goat Latin.
------------------------------------------------------------------------------------------------------

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
'''


def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    words = list(S.split(" "))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # capitalVowels = ['A', 'E', 'I', 'O', 'U']
    returnSentence = []

    for i in range(len(words)):
        newWord = ""
        if words[i][0] in vowels:
            newWord = words[i] + "maa"
            # print(newWord)
        else:
            newWord = words[i][1:] + words[i][0] + "maa"
        for j in range(i):
            newWord += "a"
        returnSentence.append(newWord)

    return ' '.join(returnSentence)