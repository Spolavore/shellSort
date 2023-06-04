
# insertion_sort modificado: dada um string
# ele ira ordenar ela e retornar a quantidade
# de trocas realizada por ele .
def insertion_sort(str):
    arr = list(str)
    arr = arr[0:len(arr)]
    trocas = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1
        arr[j + 1] = key
    return trocas



qnt_dataset = int(input())
while(qnt_dataset > 0):
    input()
    # parte do codigo que pega os dados
    # do arquivo lido e separa em variaveis inicio:
    dataset_info = input()
    quantidade_strings = int(dataset_info.split()[1])
    dataset = []
    i = 0
    while(i < quantidade_strings):
        dataset.append(input())
        i += 1
    hashMap = {} 
    #inicio da verificacao da desordenacao de cada string do dataset
    for i in range(0, quantidade_strings):
        hashMap[f'{dataset[i]}'] = insertion_sort(dataset[i])
    sorted_hash_map = sorted(hashMap.items(), key=lambda x:x[1])# funcao para ordenaro hash map
    for i in range(0, quantidade_strings):
        print(sorted_hash_map[i][0]) # print a sequencia de dna sem o \n
    print('')
    qnt_dataset -= 1
