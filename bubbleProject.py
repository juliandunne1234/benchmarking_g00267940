def bubbleSort(arrays):
    n = len(arrays)
    for outer in range(n-1, 0, -1):
        #inner loop runs one less time for each iteration to stay within loop boundaries
        for inner in range(0, outer, 1):
            #if the inner value is greater than value to the right then swap
            if arrays[inner] > arrays[inner + 1]:
                arrays[inner], arrays[inner + 1] = arrays[inner + 1], arrays[inner]
    return

#Bubblesort algorithm code adapted from youtube video @ https://www.youtube.com/watch?v=g_xesqdQqvA&t=201s
