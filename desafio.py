def insertion_sort(str):
    trocas = 0
    arr = list(str)
  #  arr = arr[0:len(arr) -1] # SOMENTO SE FOR TESTE EM ARQUIVOO
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1
        arr[j + 1] = key
    return trocas

# comente abaixo para trabalhar com arquivos
qnt_dataset = int(input())
# descomente abaixo para trabalhar com arquivos
#f = open('input612.txt', 'r') 
#qnt_dataset = int(f.readline())
outputFinal = []
while(qnt_dataset > 0):
    # comente abaixo para trabalhar com arquivos
    input()
    # descomente abaixo para trabalhar com arquivos
    #f.readline()
    # comente abaixo para trabalhar com arquivos
    dataset_info = input()
    #descomente abaixo para trabalhar com arquivos
    #dataset_info = f.readline()             
    tamanho_string = int(dataset_info.split()[0])
    quantidade_strings = int(dataset_info.split()[1])
    dataset = []
    i = 0
    while(i < quantidade_strings):
        #dataset.append(f.readline())
        dataset.append(input())
        i += 1
    itensRes = []
    for i in range(0, quantidade_strings):
        itensRes.append([{dataset[i]}, insertion_sort(dataset[i])]) 

    sortedItensRes = []
    while(len(itensRes) > 0):
        menor = ['qualquer coisa', 100000000000]
        for i in range(0, len(itensRes)):
            if(itensRes[i][1] < menor[1]):
                menor = itensRes[i]
        sortedItensRes.append(menor[0])
        indexOfMenor = itensRes.index(menor)
        itensRes.pop(indexOfMenor)
    
    for i in range(0, quantidade_strings):
        print(list(sortedItensRes[i])[0][0:tamanho_string])
    print('')
    qnt_dataset -= 1
    
