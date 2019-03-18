#! /usr/bin/python3

# Node class, with key, value, balance, and height
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None

# Put a new key value pair into a tree
def put(node, key, value):
    if node is None:
        node = Node(key, value)
        node.key = key
    else:
        if key > node.key:
            node.right = put(node.right, key, value)
        else:
            node.left = put(node.left, key, value)   
    
    node = set_heights_balance(node)
    return node
 
# Return the value given a key   
def get(node, key):
    value = get_util(node, key)
    if value is None:
        print("Not Found")
    else:
        print(value)
        
def get_util(node, key):
    value = None
    if node.key == key:
        return node.value
    if node.left is not None:
        value = get_util(node.left, key)
        if value is not None:
            return value
    if node.right is not None:
        value = get_util(node.right, key)
        if value is not None:
            return value
    return None
      
# Get the maximum height of a node
def tree_height(node): 
    if node is None: 
        return 0 
    else:
        return max(tree_height(node.left), tree_height(node.right)) + 1
  
# Level order traversal
def level_order(node):
    height = tree_height(node) 
    for i in range(1, height+1): 
        level_order_util(node, i)
    print("")

# Print a given level
def level_order_util(node, level): 
    if node is None: 
        return
    if level == 1: 
        #print(node.key, ":", node.value, "(bal=", node.balance, ")", "(hei=", node.height, ") ",end="", sep="")
        print(node.key, ":", node.value, "(", node.balance, ") ",end="", sep="")
    elif level > 1 : 
        level_order_util(node.left, level-1) 
        level_order_util(node.right, level-1)    
       
# Get the min value in a tree
def get_min(node):
    while node.left is not None:
        node = node.left
    return node
 
# Remove a node from a tree 
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
            
        temp = get_min(node.right) 
        node.value = temp.value
        node.key = temp.key
        node.right = remove(node.right, temp.key) 
    
    node = set_heights_balance_remove(node)
    return node 
    
# Update the height and balance after removing
def set_heights_balance_remove(node): 
    node.height = tree_height(node)
    left_height = 0
    right_height = 0
    if node.left is not None:
        node.left = set_heights_balance(node.left)
        left_height = node.left.height
    if node.right is not None:
        node.right = set_heights_balance(node.right)
        right_height = node.right.height
    
    # Set the balance here
    node.balance = left_height-right_height
    key = node.key
    
    # Rotation added here if the balance is off
    balance = node.balance
    
    # Left Left
    if balance > 1 and 0 <= node.left.balance: 
        node = rotate_right(node)
        set_heights_balance_remove(node)
        
    # Right Right 
    elif balance < -1 and 0 >= node.right.balance:
        node = rotate_left(node)
        set_heights_balance_remove(node)
  
    # Left Right
    elif balance > 1 and 0 < node.left.balance:
        node.left = rotate_left(node.left) 
        node = rotate_right(node)
        set_heights_balance_remove(node)
  
    # Right Left
    elif balance < -1 and 0 > node.right.balance:
        node.right = rotate_right(node.right)
        node = rotate_left(node)
        set_heights_balance_remove(node)
        
    return node

# Update the height and balance after inserting
def set_heights_balance(node): 
    node.height = tree_height(node)
    left_height = 0
    right_height = 0
    if node.left is not None:
        node.left = set_heights_balance(node.left)
        left_height = node.left.height
    if node.right is not None:
        node.right = set_heights_balance(node.right)
        right_height = node.right.height
    
    # Set the balance here
    node.balance = left_height-right_height
    key = node.key
    
    # Rotation added here if the balance is off
    balance = node.balance
    
    # Left Left
    if balance > 1 and key < node.left.key: 
        node = rotate_right(node)
        set_heights_balance(node)
        
    # Right Right 
    elif balance < -1 and key > node.right.key:
        node = rotate_left(node)
        set_heights_balance(node)
  
    # Left Right
    elif balance > 1 and key > node.left.key:
        node.left = rotate_left(node.left) 
        node = rotate_right(node)
        set_heights_balance(node)
  
    # Right Left
    elif balance < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        node = rotate_left(node)
        set_heights_balance(node)
        
    return node

# Rotate to the left
def rotate_left(node):
    right_child = node.right 
    if right_child is None:
        return node
    temp_node = right_child.left
    right_child.left = node
    node.right = temp_node
    node.height = tree_height(node)
    right_child.height =  tree_height(right_child)
    return right_child 
  
# Rotate to the right
def rotate_right(node):
    left_child = node.left 
    if left_child is None:
        return node
    temp_node = left_child.right
    left_child.right = node
    node.left = temp_node
    node.height = tree_height(node) 
    left_child.height = tree_height(left_child)
    return left_child     
       
# Set Up stuff
root = None
num_commands = int(input())

# Run ech command   
for c in range(num_commands):
    
    # Get the command and arguments
    line = input().rstrip("\n")
    command_split = line.split(" ")
    command = command_split[0]
    
    # Run the specified command
    if command == "put":
        root = put(root, int(command_split[1]), command_split[2])
    elif command == "levelorder":
        level_order(root)
    elif command == "get":
        get(root, int(command_split[1]))
    elif command == "remove":
        root = remove(root, int(command_split[1]))
