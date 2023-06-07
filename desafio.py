def insertion_sort(str):
    trocas = 0
    arr = list(str)
    #arr = arr[0:len(arr) -1] # SOMENTO SE FOR TESTE EM ARQUIVOO
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
    hashs_repetidos = [] 
    # comente abaixo para trabalhar com arquivos
    dataset_info = input()
    tamanho_string = int(dataset_info.split()[0])
    quantidade_strings = int(dataset_info.split()[1])
   # descomente abaixo para trabalhar com arquivos
   # dataset_info = f.readline()             
   # tamanho_string = int(dataset_info[0])
   # quantidade_strings = int(dataset_info.split()[1])
    dataset = []
    i = 0
    while(i < quantidade_strings):
        #dataset.append(f.readline())
        dataset.append(input())
        i += 1
    hashMap = {} 
    for i in range(0, quantidade_strings):
        if dataset[i] in hashMap:   
            hashs_repetidos.append(dataset[i]) 
        hashMap[f'{dataset[i]}'] = insertion_sort(dataset[i])

    sorted_hash_map = sorted(hashMap.items(), key=lambda x:x[1])
    for i in range(0, quantidade_strings-len(hashs_repetidos)):
        output = sorted_hash_map[i][0]
        outputFinal.append(output[0:tamanho_string])
        while output in hashs_repetidos:
            outputFinal.append(output[0:tamanho_string])
            hashs_repetidos.pop(hashs_repetidos.index(output))
    outputFinal.append('')
    qnt_dataset -= 1
for i in range(0, len(outputFinal)):
    print(outputFinal[i])