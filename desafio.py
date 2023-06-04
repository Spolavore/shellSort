import numpy as np

with open('teste.txt', 'r') as f:
    lines = f.readlines()

qnt_dataset = int(lines[0])
info = lines[1:]

while(qnt_dataset > 0):
    # parte do codigo que pega os dados
    # do arquivo lido e separa em variaveis
    dataset_info = info[0].split() 
    tamanho_strings = int(dataset_info[0])
    quantidade_strings = int(dataset_info[1])

    info = info[1:] # remove o dataset ja lido
    dataset = info[0: quantidade_strings] # pega o dataset
    print(dataset)
    info = info[quantidade_strings+1:] # pega o proximo dataset com suas informacoes
    qnt_dataset -= 1
