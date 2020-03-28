def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for k in range(len(arr) - 1 ):
            if arr[k] > arr[k+1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr
