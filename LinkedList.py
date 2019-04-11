# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:01:22 2019

@author: akash
"""

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def traverse(self):
        i=self.start
        while i is not None:
            print(i.data)
            i=i.next
            
l1=LinkedList()
l1.start=Node("Monday")
l2=Node("Tuesday")
l3=Node("Wednesday")
l4=Node("Thursday")
l5=Node("Friday")
l6=Node("Saturday")
l7=Node("Sunday")
l1.start.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=l6
l6.next=l7
l1.next=None         

#Traversing the Linked list
l1.traverse()