import random

def merger(left, right):
    
    l = r = 0
    result = []
    while (l < len(left) and r < len(right)):
        if (left[l] <= right[r]):
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
        
    while (l < len(left)):
        result.append(left[l])
        l+=1
    
    while (r < len(right)):
        result.append(right[r])
        r+=1

    return result

def mergeSort(arr):
    if (len(arr) <= 1):
        return arr

    left = mergeSort(arr[0:len(arr)//2])
    right = mergeSort(arr[len(arr)//2:len(arr)])

    return merger(left, right)


def generate_random_arr(n):
    res = []
    for i in range(n):
        res.append(random.randint(0,10))

    return res





arr = generate_random_arr(10)
arr_copy = arr.copy()





def quickSort(i, j):
    if (j <= i):
        return 
    
    pivot = partition(i,j)

    quickSort(i,pivot-1)
    quickSort(pivot+1,j)


def partition(start, end):
    pivot = arr[end]

    l = start -1
    r = start

    while (r < end):
        if (arr[r] < pivot):
            l+=1
            arr[l],arr[r] = arr[r], arr[l]

        r+=1

    l+=1
    arr[l], arr[end] = pivot, arr[l]
    
    return l

print(arr)
quickSort(0,len(arr)-1)
print(arr)
print(arr == sorted(arr_copy))
