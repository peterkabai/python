#! /usr/bin/python3

class max_heap():
    data = []

    def size(self):
        return len(self.data)

    def max_lookup(self):
        return self.data[0]

    def insert(self, value):
        self.data.append(int(value))
        length = len(self.data)
        for index in range(length, -1, -1):
            self.heapify(self.data, length, index)

    def extract_max(self):
        del self.data[0]
        length = len(self.data)
        for index in range(length, -1, -1):
            self.heapify(self.data, length, index)

    def delete(self, pos):
        del self.data[int(pos)]
        length = len(self.data)
        for index in range(length, -1, -1):
            self.heapify(self.data, length, index)

    def heapify(self, data, length, index):
        largest = index
        left = 2 * index + 1 
        right = 2 * index + 2
    
        if left < length and self.data[index] < self.data[left]: 
            largest = left 
    
        if right < length and self.data[largest] < self.data[right]: 
            largest = right
    
        if largest != index: 
            self.data[index], self.data[largest] = self.data[largest], self.data[index] 
            self.heapify(self.data, length, largest) 

class min_heap():
    data = []

    def size(self):
        return len(self.data)

    def min_lookup(self):
        return self.data[0]

    def insert(self, value):
        self.data.append(int(value))
        length = len(self.data)
        for index in range(length, -1, -1):
            self.heapify(self.data, length, index)

    def extract_min(self):
        del self.data[0]
        length = len(self.data)
        for index in range(length, -1, -1):
            self.heapify(self.data, length, index)

    def delete(self, pos):
        del self.data[int(pos)]
        length = len(self.data)
        for index in range(length, -1, -1):
            self.heapify(self.data, length, index)

    def heapify(self, data, length, index):
        smallest = index
        left = 2 * index + 1 
        right = 2 * index + 2
    
        if left < length and self.data[index] > self.data[left]: 
            smallest = left 
    
        if right < length and self.data[smallest] > self.data[right]: 
            smallest = right
    
        if smallest != index: 
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index] 
            self.heapify(self.data, length, smallest) 

print("- Test Max Heap -")
max_h = max_heap()
max_h.insert(5)
print(max_h.max_lookup())
max_h.insert(7)
print(max_h.max_lookup())
max_h.insert(10)
print(max_h.max_lookup())
max_h.extract_max()
print(max_h.max_lookup())

print("- Test Min Heap -")
min_h = min_heap()
min_h.insert(5)
print(min_h.min_lookup())
min_h.insert(1)
print(min_h.min_lookup())
min_h.insert(-1)
print(min_h.min_lookup())
min_h.extract_min()
print(min_h.min_lookup())
