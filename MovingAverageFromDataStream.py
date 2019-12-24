'''
Runtime: 104 ms, faster than 15.33% of Python online submissions for Moving Average from Data Stream.
Memory Usage: 15.1 MB, less than 60.00% of Python online submissions for Moving Average from Data Stream.



'''



class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.windowSize = size
        self.window = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window)%self.windowSize == 0:
            self.window = self.window[1:]
        self.window.append(val)
        return sum(self.window)/float(len(self.window))