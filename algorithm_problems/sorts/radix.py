def radix(arr):
    for place in range(len(str(max(arr)))):
        temp = [];
        for i in radix_util(arr, place+1, [[],[],[],[],[],[],[],[],[],[]]):
            for j in i: 
                temp.append(j);
        [print(x, end=" ") for x in temp]; 
        print()
        arr = temp
    return arr
    
def radix_util(arr, place, digits):
    for number in arr: 
        digits[int(str(number).rjust(place,'0')[-place])].append(number)
    return digits
   
# Manual testing 
# radix([170,45,75,90,2,802,2,66])
# radix([9,8,7,6,5,4,3,2,1,0,99,88,77,66,55])
# radix([9, 87, 199, 15, 3, 214, 19, 26, 58, 2, 102, 23])

# Code to for Hackerrank homework
num_values = input()
values = [int(x) for x in input().split(" ")]
radix(values)