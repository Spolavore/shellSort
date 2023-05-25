import math
def insertionSort (arr):
    for i in range (len(arr)):
        j = i
        while(j > 0):
            if(arr[j] <= arr[j-1]):
                aux = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = aux
            j -= 1

# Funcao que dado um arr e uma sequencia( shell, knuth, ciura) devolve o maior numero da sequencia que eh menor
# que o tamanho do arr
def SearchFirstGap(arr, arrSequence):
    for i in range(len(arrSequence)):
        if(len(arr) > arrSequence[i]):
            gap = arrSequence[i]
    return gap

def shellSort(arr, sequence):
    gap = SearchFirstGap(arr, sequence)
    while(gap >= 1 ):
        index = sequence.index(gap)
        for i in range(gap, len(arr)):
            j = i
            if(arr[j-gap] > arr[i]):
                temp = arr[j-gap]
                arr[j-gap] = arr[i]
                arr[i] = temp
        if(gap == 1):
            insertionSort(arr)
            gap = 0
        if(gap > 1):
            gap = sequence[index-1]
    
   
shell = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
knuth = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]

arr = [10, 41 , 5 , 4 , 76, 3, 128, 120, 30, 1 , 3  , 5 , 6 , 10]
arr2 = [9, 8, 7 , 6, 5, 4 ,3 ,2 ,1]
shellSort(arr, ciura)








