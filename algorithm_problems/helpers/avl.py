#! /usr/bin/python3

class Node:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.height = None 
        
    def rotate_right(self):
        print("Not implimented")
        
    def rotate_left(self):
        print("Not implimented")

def put(node, key, data):
    if node is None:
        node = Node(key, data)
        node.key = key
    else:
        if node.key < key:
            node.left = put(node.left, key, data)
        if node.key > key:
            node.right = put(node.right, key, data)   
    return node
    
def get(node, key):
    data = None
    if node.key == key:
        return node.data
    if node.left is not None:
        data = get(node.left, key)
        if data is not None:
            return data
    if node.right is not None:
        data = get(node.right, key)
        if data is not None:
            return data
    return data
    
def min_key(node): 
    current = node
    while(current.left is not None):
        current = current.left  
    return current 
    
def remove(node, key):
    if node is None: 
        return node
    if key < node.key: 
        node.left = remove(node.left, key) 
    elif(key > node.key): 
        node.right = remove(node.right, key) 
    else:
        if node.left is None : 
            temp = node.right  
            node = None 
            return temp  
        elif node.right is None : 
            temp = node.left  
            node = None
            return temp
        temp = min_key(node.right)
        node.key = temp.key
        node.right = remove(node.right , temp.key) 
    return node 
  
def tree_height(node): 
    if node is None: 
        return 0 
    else:
        left = tree_height(node.left) 
        right = tree_height(node.right) 
        if left > right: 
            return left+1
        else: 
            return right+1
  
def level_order(node):
    height = tree_height(node) 
    for i in range(1, height+1): 
        print_level(node, i)

def print_level(node, level): 
    if node is None: 
        return
    if level == 1: 
        print(node.data)
    elif level > 1 : 
        print_level(node.left, level-1) 
        print_level(node.right, level-1) 











def pretty_print(node):
    height = tree_height(node) 
    max_height = tree_height(node)
    for i in range(1, height+1):
        # for j in range(int(round(2^(max_height-height))/2)):
        #     output.append(" ")
        print(pretty_print_level(node, i))
        
        

def pretty_print_level(node, level): 
    
    
    if node is None: 
        #output.extend(" ")
        return None
    if level == 1: 
        
        return node.data 
        
    elif level > 1 : 
        
        height -= 1
        pretty_print_level(node.left, level-1) 
        pretty_print_level(node.right, level-1)
        output.extend(" ")   
    
            
        
        
        
        
root = None
root = put(root, 5,'a')
root = put(root, 3,'b')
root = put(root, 2,'c')
root = put(root, 9,'d')
root = put(root, 1,'e')
root = put(root, 7,'f')
root = put(root, 0,'g')

# print(get(root, 2))
# print("---")
# level_order(root)
pretty_print(root)
#
print("---")
root = remove(root, 1)
pretty_print(root)
