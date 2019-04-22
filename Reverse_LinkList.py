# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:40:05 2019

@author: akash
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        c = head
        n = None
        while(c != None):
            n = c.next
            c.next = p
            p=c
            c = n
        head = p
        return(head)