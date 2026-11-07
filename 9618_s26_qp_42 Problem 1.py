def FindLongestShortest(array):
    longest, shortest = array[0], array[0]
    for i in range(len(array)):
        if len(array[i]) < len(shortest):
            shortest = array[i]
        elif len(array[i]) > len(longest):
            longest = array[i]
    print(longest)
    print(shortest)

def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j>=0 and array[j].lower() > key.lower():
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


TheData = ["laptop", "tablet", "printer", "computer",
           "processor", "monitor", "memory", "cable",
           "touchscreen"]

FindLongestShortest(TheData)
print("Before sorting")
print(TheData)
sorted_array = InsertionSort(TheData)
print("After sorting")
print(sorted_array)