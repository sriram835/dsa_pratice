import random

def merge_sort(arr):
    
    if (len(arr) == 1):
        return arr


    mid = (len(arr))//2

    arr1 = merge_sort(arr[:mid]);
    arr2 = merge_sort(arr[mid:]);

    return arr_merge(arr1,arr2)

    



def arr_merge(arr1,arr2):
    ptr1 = 0
    ptr2 = 0
    arr = []
    while (ptr1 < len(arr1) and ptr2 < len(arr2)):
        if (arr1[ptr1] < arr2[ptr2]):
            arr.append(arr1[ptr1])
            ptr1+=1
        else:
            arr.append(arr2[ptr2])
            ptr2+=1

    if (ptr2 < len(arr2)):
        for i in range(ptr2,len(arr2)):
            arr.append(arr2[i])

    if (ptr1 < len(arr1)):
        for i in range(ptr1,len(arr1)):
            arr.append(arr1[i])

    return arr
    


def generate_random_arr(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1,10))
    return arr

arr1 = [1]

arr2 = [2]

arr = generate_random_arr(10)

print(arr)

sorted_arr = merge_sort(arr.copy())

print(sorted_arr)
print(sorted_arr == sorted(arr))

