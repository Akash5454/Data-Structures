# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:20:42 2019

@author: akash
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def Insert(self,val):
        if self.data:
            if val <= self.data:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.Insert(val)
            elif(val > self.data):
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.Insert(val)
        else:
            self.data = val
    def pre(self,root):
        output = []
        if root:
            output.append(root.data)
            output = self.pre(root.left)
            output = output + self.pre(root.right)
        return(output)
    def ino(self,root):
        output = []
        if root:
            output = self.ino(root.left)
            output.append(root.data)
            output = output + self.ino(root.right)
        return(output)
    def post(self,root):
        output = []
        if root:
            output = self.post(root.left)
            output = output + self.post(root.right)
            output.append(root)
        return(output)
root = Node(8)
root.Insert(3)
root.Insert(10)
root.Insert(1)
root.Insert(6)
root.Insert(14)
root.Insert(4)
root.Insert(7)
root.Insert(3)
print(root.ino(root))        
print(root.pre(root))        
print(root.post(root))            
            
                
                
                            
            
            
            