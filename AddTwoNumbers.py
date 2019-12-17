'''

Runtime: 60 ms, faster than 45.99% of Python online submissions for Add Two Numbers.
Memory Usage: 11.9 MB, less than 21.32% of Python online submissions for Add Two Numbers.
------------------------------------------------------------------------------------------

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
# add the 2 current nodes, plus the carry of the previous addition.
# then add the remainder of each list.
# finish by adding the remaining carry value.

# ----------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        list1, list2 = l1, l2
        returnNode = ListNode(0)
        newListNode = returnNode
        carry = 0
        while True:
            sum = (list1.val + list2.val + carry)
            newVal = sum % 10
            carry = sum // 10
            newListNode.next = ListNode(newVal)
            newListNode = newListNode.next
            if list1.next == None or list2.next == None:
               break 
            list1, list2 = list1.next, list2.next
        
        while list1.next != None:
            list1 = list1.next
            sum = (list1.val + carry)
            newVal = sum % 10
            carry = sum // 10
            newListNode.next = ListNode(newVal)
            newListNode = newListNode.next
            

        while list2.next != None:
            list2 = list2.next
            sum = (list2.val + carry)
            newVal = sum % 10
            carry = sum // 10
            newListNode.next = ListNode(newVal)
            newListNode = newListNode.next
            

        if carry != 0:
            newListNode.next = ListNode(carry)


        return returnNode.next
            
        