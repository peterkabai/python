#! /usr/bin/python3

import fileinput


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            # if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
            # elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data


COUNT = [10]


def print_tree(tree_root, space=0):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print_tree(tree_root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print("end")
    print(tree_root.data)

    # Process left child
    print_tree(tree_root.left, space)


# do binary search here
def from_array(arr, tree_root, i, n):
    # Base case for recursion
    if i < n:
        temp = Node(arr[i])
        tree_root = temp

        # insert left child
        tree_root.left = from_array(arr, tree_root.left, 2 * i + 1, n)

        # insert right child
        tree_root.right = from_array(arr, tree_root.right, 2 * i + 2, n)
    return tree_root


def to_array(tree_root):
    if tree_root is None:
        return []
    return to_array(tree_root.left) + [tree_root.data] + to_array(tree_root.right)


INT_MAX = 4294967296
INT_MIN = -4294967296


def is_bst(tree_root):
    if is_bst_util(tree_root, INT_MIN, INT_MAX):
        print("true")
    else:
        print("false")


def is_bst_util(node, mini, maxi):
    # An empty tree is BST 
    if node is None:
        return True
    return (is_bst_util(node.left, mini, node.data - 1) and
            is_bst_util(node.right, node.data + 1, maxi))


def pre_order(tree_root):
    print("preOrder")
    return -1


def post_order(tree_root):
    print("postOrder")
    return -1


def num_nodes_in_lookup(num):
    print("numNodesInLookup " + str(num))
    return -1


line_num = 1

for line in fileinput.input(["completeTrees.txt"]):

    num_elements = -1

    if line_num == 1:
        num_elements = int(line)
    elif line_num == 2:

        # create tree here
        values = line.rstrip("\n\r").split(" ")
        print(values)
        root = Node(num_elements)
        root = from_array(values, root, 0, num_elements)
        # root = Node(num_elements)
        # for value in val:
        #     root.insert(int(value))
        print(root)
        print_tree(root)

    elif line_num > 3:

        command = line.rstrip("\n").split(" ")[0]

        switcher = {
            "fromArray": from_array,
            "toArray": to_array,
            "isBST": is_bst,
            "preOrder": pre_order,
            "postOrder": post_order,
            "numNodesInLookup": num_nodes_in_lookup
        }
        func = switcher.get(command, lambda: "Invalid command")

        if command == "numNodesInLookup":
            func(line.rstrip("\n").split(" ")[1])
        else:
            print(root)
            print(func(root))

    line_num = line_num + 1
