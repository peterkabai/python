#! /usr/bin/python3

class node:
    def __init__(self, data):
        self.data = data
        self.key = None
        self.left = None
        self.right = None
        self.height = None 
        
def get_height(root):
    print("Not implimented")
    
def level_order_trav(root):
    print("Not implimented")
    
def is_balanced(root):
    print("Not implimented")

def create_from_arr(arr, i=0, root=None): 
    if i < len(arr): 
        temp = node(arr[i])  
        root = temp  
  
        # Insert left child  
        root.left = create_from_arr(arr,  2 * i + 1, root.left)  
  
        # Insert right child  
        root.right = create_from_arr(arr,  2 * i + 2, root.right) 
    return root 
    
def pre_order_trav(root):
    print(root.data)
    if root.left is not None:
        pre_order_trav(root.left)
    if root.right is not None:
        pre_order_trav(root.right)
    
def in_order_trav(root):
    if root.left is not None:
        pre_order_trav(root.left)
    print(root.data)
    if root.right is not None:
        pre_order_trav(root.right)
        
def post_order_trav(root):
    if root.left is not None:
        pre_order_trav(root.left)
    if root.right is not None:
        pre_order_trav(root.right)
    print(root.data)
    
    
# Create a test tree
root = create_from_arr([1,2,3,4,5,6,7])
    
# Test expressions
print(root.right.right.data)
print("---")
pre_order_trav(root)
print("---")
in_order_trav(root)