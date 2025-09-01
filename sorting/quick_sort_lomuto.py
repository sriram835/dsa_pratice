import random



def quick_sort(arr,start,end):
    if (end <= start):
        return

    pivot = partition(arr,start,end)

    quick_sort(arr,start,pivot-1)
    quick_sort(arr,pivot+1,end)



def partition(arr,start, end):
    

    pivot = arr[end]

    l = start -1
    r = start

    while (r <= end-1):
        if (arr[r] < pivot):
            l+=1
            arr[l],arr[r] = arr[r], arr[l]

        r+=1

    l+=1
    arr[l], arr[end] = pivot, arr[l]
    
    return l


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

