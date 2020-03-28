from selection_sort import selection_sort
from bubble_sort import bubble_sort


arr = [2, 53, 1, 66, 22, 20]


if __name__ == "__main__":
    print("BEFORE SORT", arr, sep="\n")
    #sort algorithm
    #selection_sort(arr)
    bubble_sort(arr)
    #sort algorithm
    print("AFTER SORT", arr, sep="\n")
