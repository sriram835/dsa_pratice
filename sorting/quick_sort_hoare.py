import random

def quick_sort(arr,start,end):
    
    if (end <= start):
        return

    pivot = partition(arr,start,end)

    quick_sort(arr,start,pivot-1)
    quick_sort(arr,pivot+1,end)


def partition(arr, start, end):

    pivot = arr[start]

    l = start
    r = end 

    while (l < r):
        
        while (arr[l] <= pivot and l <= end -1):
            l+=1

        while (arr[r] > pivot and r >= start+1):
            r-=1
        
        if (l < r):
            arr[l], arr[r] = arr[r], arr[l]

    
    arr[r], arr[start] = pivot, arr[r]

    return r


def generate_random_arr(n):
    arr = []

    for i in range(n):
        arr.append(random.randint(1,10))

    return arr

arr = generate_random_arr(10)

print(arr)
sorted_arr = arr.copy()
quick_sort(sorted_arr,0,len(sorted_arr)-1)
print(sorted_arr)
print(sorted_arr == sorted(arr))
