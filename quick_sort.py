def partition_element(arr, low, high) :
    pivot = arr[low]
    i = low
    j = high
    while i < j :
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    arr[low], arr[j] = arr[j], arr[low]
    return j 
def quick_sort(arr, low, high) :
    if low < high :
        partition = partition_element(arr, low, high)
        quick_sort(arr, low, partition - 1)
        quick_sort(arr, partition + 1, high)
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(f"The sorted array is : {arr}")
