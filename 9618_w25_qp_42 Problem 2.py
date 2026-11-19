import random


def PrintArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def BubbleSort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr


def RecursiveBinarySearch(arr, l_bound, h_bound, x):
    if l_bound <= h_bound:
        mid = (l_bound + h_bound) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return RecursiveBinarySearch(arr, l_bound, mid - 1, x)
        else:
            return RecursiveBinarySearch(arr, mid + 1, h_bound, x)
    else:
        return -1


array = [random.randint(0, 100) for _ in range(20)]
PrintArray(array)
print("Sorted")
PrintArray(BubbleSort(array))
value = int(input("Enter an integer: "))
if RecursiveBinarySearch(array, 0, len(array) - 1, value) == -1:
    print("Not found")
else:
    print(f"Found at position {RecursiveBinarySearch(array, 0, len(array) - 1, value)}")