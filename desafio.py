
# insertion_sort modificado: dada um string
# ele ira ordenar ela e retornar a quantidade
# de trocas realizada por ele .
def insertion_sort(str):
    arr = list(str)
    arr = arr[0:len(arr)-1]
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


# parte de leitura de arquivo e obtencao da quantidade
# de datasets e informacoes utilizaveis
with open('inputs.txt', 'r') as f:
    lines = f.readlines()


qnt_dataset = int(lines[0])
info = lines[2:]

while(qnt_dataset > 0):
  
# parte do codigo que pega os dados
# do arquivo lido e separa em variaveis inicio:
    dataset_info = info[0].split() 
    tamanho_strings = int(dataset_info[0])
    quantidade_strings = int(dataset_info[1])
    info = info[1:] # remove as informacoes de tamanho_string e quantidade_strings ja lida
    dataset = info[0: quantidade_strings] # pega o dataset
    
    hashMap = {} 
#inicio da verificacao da desordenacao de cada string do dataset
    for i in range(0, quantidade_strings):
        hashMap[f'{dataset[i]}'] = insertion_sort(dataset[i])

    sorted_hash_map = sorted(hashMap.items(), key=lambda x:x[1])# funcao para ordenaro hash map

    for i in range(0, quantidade_strings):
        print((sorted_hash_map[i][0][0:tamanho_strings-1])) #print a sequencia de dna sem o \n

    print('')
# pega o proximo dataset com suas informacoes removendo a blank line
    info = info[quantidade_strings+1:] 
    qnt_dataset -= 1

