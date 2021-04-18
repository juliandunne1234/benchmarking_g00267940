def countSort(arrays):
    
    #Determine the number range
    max_element = int(max(arrays))
    min_element = int(min(arrays))
    range_of_elements = max_element - min_element + 1
    
    #Create empty index of size number range to store the number count of individual elements
    count_arr = [0 for _ in range(range_of_elements)]
    #output array to store the sorted list
    output_arr = [0 for _ in range(len(arrays))]
 
    #Fill index array with the element frequency
    #Note: Index array counts by index value and stores by order of index not by the order of the element in the array
    for i in range(0, len(arrays)):
        count_arr[arrays[i]-min_element] += 1
 
    #Add the index array value with the value of its predecessor
    #The index array now contains actual position of the element in the output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    #Map index array to the output array
    #Subtract 1 from index value in array - required for index position eg. if number appears twice in array
    for i in range(len(arrays)-1, -1, -1):
        output_arr[count_arr[arrays[i] - min_element] - 1] = arrays[i]
        count_arr[arrays[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arrays)):
        arrays[i] = output_arr[i]
 
    return arrays

#countSort algorithm code taken from website link @ https://www.geeksforgeeks.org/counting-sort/
#countSort algorithm code step by step understanding found on youtube video link @ https://www.youtube.com/watch?v=0B33As8jPgo
