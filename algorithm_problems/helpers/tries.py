class node:
    def __init__(self, char="", leaf=False):
        self.char = char
        self.leaf = leaf
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
       
    def lookup(self, word, ret_node=False):
        for child in self.children:
            if child.char == word[0]:
                return child.lookup_util(word, ret_node)

    def lookup_util(self, word, ret_node=False):
        # Move on if the first char of the word matches
        if self.char == word[0]:
            
            # If we're using this to check for autocomplete
            if ret_node and word is self.char:
                return self
            
            # If there's a valid match
            if word is self.char and self.leaf:
                return 1
                
            # If no word match and there are still chars left
            if len(word) > 1:
                
                # Strip the first char
                word = word[1:]
                for child in self.children:
                    
                    # If the char of the child matches, do a recursive call
                    if child.char == word[0]:
                        return child.lookup_util(word, ret_node)
                        
        # No match to word or partial word
        return 0
    
    def insert_util(self, word):

        # If the word is of length 1
        if len(word) == 1: 
            has_corrent_child = False
            for child in self.children:
                if child.char == word:
                    has_corrent_child = True
                    child.leaf = True
            if not has_corrent_child:
                self.add_child(node(word, True))
            
        # If the word is still longer
        else:
            has_corrent_child = False
            for child in self.children:
                if child.char == word[0]:
                    has_corrent_child = True
                    child.insert_util(word[1:])
            if not has_corrent_child:
                new_child = node(word[0])
                new_child.insert_util(word[1:])
                self.add_child(new_child)
                    
    def insert(self, word):
        self.insert_util(word)
                    
    def alphabetical(self, autocomplete=False):
        all_words = self.alphabetical_util([])
        all_words.sort()
        if autocomplete:
            return all_words
        else:
            print(("\n").join(all_words))
    
    def alphabetical_util(self, visited, words=[], level=0):
        visited = visited[0:level]
        visited.append(self.char)
        if self.leaf:
            words.append(("").join(visited))
        for child in self.children:
            words = list(set(child.alphabetical_util(visited, words, level+1)))
        return words
            
    def info(self):
        values = self.info_util()
        print(values[0]-1, values[1])
        
    def info_util(self, num=1, words=0):
        num += 1
        if self.leaf:
            words += 1
        for child in self.children:
            num, words = child.info_util(num, words)
        return num, words
        
    def autocomplete(self, prefix, k):
        none_found = True
        for child in self.children:
            if child.char == prefix[0]:
                child.autocomplete_util(prefix, k)
                none_found = False
                break
        if none_found: print("")

    def autocomplete_util(self, prefix, k):
        words = self.alphabetical(True)
        if k == -1:
            parts = []
            for word in words:
                if len(prefix) <= len(word) and word[0:len(prefix)] == prefix:
                    parts.append(word)
            print((" ").join(parts))

        else:
            parts = []
            for word in words:
                if len(prefix) <= len(word) and len(word) <= len(prefix) + k and word[0:len(prefix)] == prefix:
                    parts.append(word)
            print((" ").join(parts))

    def remove(self, word):
        for child in self.children:
            if child.char == word[0]:
                return child.remove_util(word)

    def remove_util(self, word):
        
        # Move on if the first char of the word matches
        if self.char == word[0]:
              
            # If no word match and there are still chars left
            if len(word) > 1:
                
                # Strip the first char
                word = word[1:]
                child_num = 0
                for child in self.children:
                    
                    # If the char of the child matches, do a recursive call
                    if child.char == word[0] and len(word) == 1 and child.leaf:
                        child.leaf = False
                        if len(child.children) == 0:
                            self.children.pop(child_num)
                            return True

                    elif child.char == word[0]:
                        removed = child.remove_util(word)
                        if removed:
                            if len(child.children) == 0 and not child.leaf:
                                self.children.pop(child_num)
                                return True
                        return False

                    child_num += 1
         
# Driver code for Hackerrank
root = node()
num_lines = int(input())
for num in range(num_lines):
    line = input().split(" ")
    if line[0] == "insert":
        root.insert(line[1])
    elif line[0] == "lookup":
        print(root.lookup(line[1]))
    elif line[0] == "alphabetical":
        root.alphabetical()
    elif line[0] == "info":
        root.info()
    elif line[0] == "autocomplete":
        root.autocomplete(line[1], int(line[2]))
    elif line[0] == "remove":
        root.remove(line[1])
    
# Local Test Code
# root = node()
# root.insert("james")
# root.insert("jackie") 
# print(root.look("ja"))          
# root.insert("ja")     
# print(root.look("ja"))           
# root.insert("jay")        
# root.insert("jane")  
# print(root.look("jackie"))           
# root.alphabetical()
# root.info()
# root.autocomplete("ja", 2)
# root.autocomplete("ja", -1)
# root.remove("jackie")
# print(root.look("jackie")) 
# print(root.look("ja"))   
# root.alphabetical()
# root.info()
