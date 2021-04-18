def selectionSort(arrays):
    n = len(arrays)
    for outer in range(0, n-1, 1):
        #set the min index value
        min = outer
        #loop through the inner index values starting from outer+1
        for inner in range(outer+1, n, 1):
            #check if inner value is less than the arr[min] value and set lowest value as index
            if arrays[inner] < arrays[min]:
                min = inner
        #if the min index is not equal to the outer index then reorganise values accordingly 
        if min != outer:
            arrays[min], arrays[outer] = arrays[outer], arrays[min]
    return

#Selectionsort algorithm code adapted from Derrick Sherrill youtube video @ https://www.youtube.com/watch?v=4CykZVqBuCw&t=244s