class TrieNode:
    def __init__(self, val):
        self.val = val
        self.neighbor = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,word):
        temp = self.root
        for letter in word:
            if letter not in temp.neighbor:
                temp.neighbor[letter] = TrieNode()
            temp = temp.neighbor[letter]    
        temp.isEnd = True
 
            
                
                
        

    


        
        
        
                
        



        
    