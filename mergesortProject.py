def mergeSort(arrays):

    #base case and recursive function
    #array length > 1 then seperate into 2 arrays
    if len(arrays) > 1:
        mid = len(arrays)//2
        lefthalf = arrays[:mid]
        righthalf = arrays[mid:]

        #recursive call
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        #set index of left/right/k arrays
        i = 0
        j = 0
        k = 0

        #while loop required for performing comparison multiple times
        #and merging the subarrays
        while i < len(lefthalf) and j < len(righthalf):
            #if lefthalf[i] is less than righthalf[j] then place in arr[k]
            if lefthalf[i] < righthalf[j]:
                arrays[k] = lefthalf[i]
                i += 1
            #else place righthalf[j] in arr[k]
            else:
                arrays[k] = righthalf[j]
                j += 1
            k += 1
    
        #check that to see if a value has been left out from the lefthalf subarray
        while i < len(lefthalf):
            arrays[k] = lefthalf[i]
            i += 1
            k += 1
        
        #check that to see if a value has been left out from the righthalf subarray
        while j < len(righthalf):
            arrays[k] = righthalf[j]
            j += 1
            k += 1

    return

#Mergesort algorithm code taken from website link @  https://www.pythoncentral.io/merge-sort-implementation-guide/
#Mergesort algorithm code explanation from youtube video @ https://www.youtube.com/watch?v=_trEkEX_-2Q

