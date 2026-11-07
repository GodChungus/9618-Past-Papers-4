def FindLongestShortest(array):
    longest, shortest = array[0], array[0]
    for i in range(len(array)):
        if len(array[i]) < len(shortest):
            shortest = array[i]
        elif len(array[i]) > len(longest):
            longest = array[i]
    print(longest)
    print(shortest)


TheData = ["laptop", "tablet", "printer", "computer",
           "processor", "monitor", "memory", "cable",
           "touchscreen"]

FindLongestShortest(TheData)