#! /usr/bin/python3

# https://csumb.kattis.com/problems/pivot

count = int(input())
numbers = list(map(int, input().split()))
pivots = 0

left = [0 for _ in range(count)]
left[0] = 0
for i in range(1, count):
    left[i] = max(left[i - 1], numbers[i - 1])

right = [2**32 - 1 for _ in range(count)]

for i in range(count - 2, -1, -1):
    right[i] = min(right[i + 1], numbers[i + 1])

for i in range(count):
    if numbers[i] >= left[i] and numbers[i] < right[i]:
        pivots += 1

print(pivots)
    
# --- Sample 1 ---
# 8
# 2 1 3 4 7 5 6 8

# 3

# --- Sample 2 ---
# 7
# 1 2 3 4 5 7 6

# 5

# --- Sample 3 ---
# 10
# 1 2 3 4 5 6 7 8 9 10

# 10