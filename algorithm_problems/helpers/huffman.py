from collections import Counter
import heapq 
  
class Node():
    def __init__(self, left, right, c, freq):
        self.left = left
        self.right = right
        self.freq = freq
        self.c = c

    def __gt__(self, other):
        return self.freq > other.freq

    def __lt__(self, other):
        return self.freq < other.freq

def get_frequencies(string):
    frequencies = []
    char_freq = dict(Counter(string))
    for char, freq in char_freq.items():
        frequencies.append((char, freq))
    frequencies = sorted(frequencies, key = lambda x: x[0])
    return frequencies

def create_huff(string):
    freq = get_frequencies(string)
    list_nodes = []
    for i in freq:
        n = Node(None, None, i[0], i[1])
        heapq.heappush(list_nodes, n)
    while len(list_nodes) > 1:
        left = heapq.heappop(list_nodes)
        right = heapq.heappop(list_nodes)
        n = Node(left, right, "$", left.freq + right.freq)
        heapq.heappush(list_nodes, n)
    return heapq.heappop(list_nodes)

def get_dictionary(node, value="", dictionary={}):
    if node.right is not None:
        get_dictionary(node.right, value+"1", dictionary)
    if node.left is not None:
        get_dictionary(node.left, value+"0", dictionary)
    if (node.right is None) and (node.left is None):
        dictionary[node.c] = value
    return(dictionary)

def print_encoded(dictionary, string):
  comp = ""
  for char in string:
    comp += dictionary[char]
  print(comp)

def print_decoded(input_str, tree, result=""):
  node = tree
  for num in input_str:
    if num == "0":
      node = node.left
    else:
      node = node.right
    if node.right is None and node.left is None:
      result += node.c
      node = tree
  print(result)

# Inputs
source_string = "hello, world!"
result_string = "00010000101111101110111011"

# Creating the tree and dictionary
tree = create_huff(source_string)
dictionary = get_dictionary(tree)

# Testing our code
print("Our dictionary:")
print(dictionary)
print("Encoded decoded string:")
print_encoded(dictionary, source_string)
print("Decoded encoded string:")
print_decoded(result_string, tree)
