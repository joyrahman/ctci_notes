

class Node:
    def __init__(self):
        self.keys = dict()
        self.isValid = False
        self.count = 0

class Trie:
    root = None
    def __init__(self):
        self.root = Node()
    def public_add_contact(self,contact):
        #self.add_contact(self.root, contact,0)
        self.add_contact3(self.root, contact)


    
    def add_contact( self,current_node, word, current_index):
        # base case: end of string reached
        if current_index ==len(word):
            current_node.isValid = True
            current_node.count = 1
            return
        # other case: check if current node has an entry for the character 
        ch = word[current_index]
        temp = current_node.keys.get(ch,None)
        if temp == None:
            temp = Node()
            current_node.keys[ch] = temp
        current_node.count += 1
        self.add_contact (temp, word, current_index+1)

    def public_find_contact(self,prefix):
        #count = self.find_contact(self.root, prefix,0)
        count = self.find_contact3(self.root, prefix)


        #print result
        return count
        #return len(result)
        
        
    def find_contact2(self,current_node, prefix, current_index):
        # check base case
        count  = 0
        if current_index == len(prefix):
            # we have consumed the whole prefix
            # do a traversal
            '''
            result = []
            if len(current_node.keys) >0 and current_node.isValid  == True:
                result.append(prefix)
            if len(current_node.keys)==0 and current_node.isValid == True:
                return prefix
            '''
            if current_node.isValid == True:
                count +=1
            if len(current_node.keys)==0:
                return count
            for current_key,next_node in current_node.keys.items():
                next_prefix = prefix + current_key
                next_index = current_index + 1
                count += self.find_contact(next_node, next_prefix, next_index )
                #if item!=[]:
                #    result.append(item)
            
            return count
                
            
        # else
        ch = prefix[current_index]
        temp = current_node.keys.get(ch,None)
        
        # if not found key
        if temp == None:
            #return []
            return 0
        
        return self.find_contact(temp, prefix, current_index +1)
    
    def find_contact(self,current_node, prefix, current_index):
        if current_index == len(prefix):
            return current_node.count
        ch = prefix[current_index]
        temp = current_node.keys.get(ch,None)
        if temp == None:
            return 0
        return self.find_contact (temp, prefix, current_index+1)

    def find_contact3(self,current_node,prefix):
        current_index  = 0
        target = len(prefix)
        while (current_index!= target):
            ch = prefix[current_index]
            next_node = current_node.keys.get(ch,None)
            if next_node == None:
                return 0
            
            current_node = next_node
            current_index +=1
        return current_node.count
    
    
    def add_contact3(self,current_node,prefix):
        current_index  = 0
        target = len(prefix)
        while (current_index!= target):
            ch = prefix[current_index]
            next_node = current_node.keys.get(ch,None)
            if next_node == None:
                next_node = Node()
                current_node.keys[ch] = next_node
            
            current_node.count += 1
            current_node = next_node
            current_index +=1
        
        current_node.isValid = True
        current_node.count += 1
    
    
    
#main method
n = int(raw_input().strip())
t = Trie()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')    
    if op=="add":
        t.public_add_contact(contact)
    elif op=="find":
        print t.public_find_contact(contact)
