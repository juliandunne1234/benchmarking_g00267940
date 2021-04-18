def quickSort(arrays):
    length = len(arrays)
    #if length not greater than 1 return array
    if length <= 1:
        return arrays
    #pop method to select an element in the array and set as the pivot variable
    else:
        pivot = arrays.pop()
    
    items_greater = []
    items_lower = []

    #value greater/less than pivot are seperated in different arrays    
    for item in arrays:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    #recursively loop through the new lists until the logic breaks where array length is <= 1
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

#Quicksort algorithm code adapted from Derrick Sherrill youtube video @ https://www.youtube.com/watch?v=kFeXwkgnQ9U