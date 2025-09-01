import random


def threeWayQuickSort(arr,low,high):
    
    
    if (low >= high):
        return


    random_index = random.randint(low,high)
    pivot = arr[random_index][1]



    i = j = k = low
    c = low

    while (k <= high and c <=high):
        if (arr[c][1] < pivot):
            arr[c], arr[k] = arr[k], arr[c]
            arr[k], arr[j] = arr[j], arr[k]
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j+=1
            k+=1
            c+=1

        elif (arr[c][1] == pivot):
            arr[c], arr[k] = arr[k], arr[c]
            arr[k], arr[j] = arr[j], arr[k]

            j+=1
            k+=1
            c+=1

        else:
            arr[k], arr[c] = arr[c], arr[k]
            k+=1
            c+=1

    threeWayQuickSort(arr, low, i-1)
    threeWayQuickSort(arr,j,high)

def is_sorted_by_value(order_list):
    for i in range(1, len(order_list)):
        if order_list[i-1][1] > order_list[i][1]:
            return False
    return True

def generate_random_orders(n):
    orders = []
    for i in range(n):
        orders.append([ f"ORD{10001+i}", random.randint(2000,5000)])

    return orders


orders = generate_random_orders(10000)

threeWayQuickSort(orders, 0, len(orders)-1)


print(is_sorted_by_value(orders))
