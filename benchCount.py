#Import as required
import random
import bubbleProject
import selectionProject
import quicksortProject
import mergesortProject
import countsortProject
import sortTime
import pandas as pd
import matplotlib.pyplot as plt

#main function that lists the benchmark population sizes
#and calls functions in the required order 
def main():
    benchArray = [200, 400, 1000, 2000, 5000, 10000, 15000]
    data = bencharrFun(benchArray)
    dataFrame = dataframeFun(data, benchArray)
    
#function that loops through the benchmark population sizes
def bencharrFun(benchArray):
    benchmarkArr = []
    for bench in benchArray:
        benchTest = genArray(bench)
        benchmarkArr.append(benchTest)
    return benchmarkArr

#function that runs i number of iterations
#sorting the random arrays during each iteration
#and finding the average sorting time for each algotrithm
def genArray(bench):
    bubblestartCount = 0
    selectionstartCount = 0
    quicksortstartCount = 0
    mergesortstartCount = 0
    countsortstartCount = 0
    i = 1
    while i <= 10:
        #bubbleSort
        bubbleArrays = random_array(bench)
        bubblerunTime = sortTime.bubblerunTime(bubbleArrays)
        bubblestartCount = bubblestartCount + bubblerunTime
        #selectionSort
        selectionArrays = random_array(bench)
        selectionrunTime = sortTime.selectionrunTime(selectionArrays)
        selectionstartCount = selectionstartCount + selectionrunTime
        #quickSort
        quicksortArrays = random_array(bench)
        quicksortrunTime = sortTime.quicksortrunTime(quicksortArrays)
        quicksortstartCount = quicksortstartCount + quicksortrunTime
        #mergeSort
        mergesortArrays = random_array(bench)
        mergesortrunTime = sortTime.mergesortrunTime(mergesortArrays)
        mergesortstartCount = mergesortstartCount + mergesortrunTime
        #countSort
        countsortArrays = random_array(bench)
        countsortrunTime = sortTime.countsortrunTime(countsortArrays)
        countsortstartCount = countsortstartCount + countsortrunTime

        i += 1

    bubbleaverageTime = round((bubblestartCount/10), 3)
    selectionaverageTime = round((selectionstartCount/10), 3)
    quicksortaverageTime = round((quicksortstartCount/10), 3)
    mergesortaverageTime = round((mergesortstartCount/10), 3)
    countsortaverageTime = round((countsortstartCount/10), 3)
    return bubbleaverageTime, selectionaverageTime, quicksortaverageTime, mergesortaverageTime, countsortaverageTime

#function that generates the pseudo random arrays of integers
def random_array(bench):
    array = []
    for i in range (0, bench, 1):
        array.append(random.randint(0,100))
    return array

#function that generates a dataframe for the average run times
#for each sorting algotrithm of sample size 'size'
#output a graph and csv file 
def dataframeFun(data, benchArray):
    df = pd.DataFrame(data, columns = ['BubbleSort', 'SelectionSort', 'QuickSort', 'MergeSort', 'CountSort'], index = benchArray)
    df.index.name = 'Size'
    df.to_csv('average_execution_times.csv')
    plt.plot(df['BubbleSort'], '-o', label='BubbleSort')
    plt.plot(df['SelectionSort'], '-o', label='SelectionSort')
    plt.plot(df['QuickSort'], '-o', label='QuickSort')
    plt.plot(df['MergeSort'], '-o', label='MergeSort')
    plt.plot(df['CountSort'], '-o', label='CountSort')
    plt.xlabel('Population size')
    plt.ylabel('Execution time in seconds')
    plt.legend(loc='upper left')
    plt.grid()
    plt.savefig('average_execution_times.jpg')
    plt.show()

#call the main function
if __name__ == "__main__":
    main()