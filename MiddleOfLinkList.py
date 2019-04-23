# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:07:26 2019

@author: akash
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = head
        j = i
        while(j != None and j.next != None):
            i = i.next
            j = j.next.next
        return(i)