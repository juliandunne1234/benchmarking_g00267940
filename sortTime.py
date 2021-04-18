import time
import bubbleProject
import selectionProject
import quicksortProject
import mergesortProject
import countsortProject

#funtion that counts the time taken to execute the bubble sort algorithm on an unordered array
def bubblerunTime(arrays):
    startTime = time.time()
    bubbleProject.bubbleSort(arrays)
    endTime = time.time()
    bubbleTime = endTime - startTime
    return bubbleTime

#funtion that counts the time taken to execute the selection sort algorithm on an unordered array
def selectionrunTime(arrays):
    startTime = time.time()
    selectionProject.selectionSort(arrays)
    endTime = time.time()
    selectionTime = endTime - startTime
    return selectionTime

#funtion that counts the time taken to execute the quick sort algorithm on an unordered array
def quicksortrunTime(arrays):
    startTime = time.time()
    quicksortProject.quickSort(arrays)
    endTime = time.time()
    quicksortTime = endTime - startTime
    return quicksortTime

#funtion that counts the time taken to execute the merge sort algorithm on an unordered array
def mergesortrunTime(arrays):
    startTime = time.time()
    mergesortProject.mergeSort(arrays)
    endTime = time.time()
    mergesortTime = endTime - startTime
    return mergesortTime

#funtion that counts the time taken to execute the count sort algorithm on an unordered array
def countsortrunTime(arrays):
    startTime = time.time()
    countsortProject.countSort(arrays)
    endTime = time.time()
    countsortTime = endTime - startTime
    return countsortTime