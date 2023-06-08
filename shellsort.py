import time
import sys

# Funcao que dado um arr e uma sequencia(shell, knuth, ciura) devolve parte da sequencia tal que o ultimo nº seja menor
# que o tamanho do arr
def ChoosenSequence(arr, arrSequence):
    for i in range(len(arrSequence)):
        if(len(arr)-1 < arrSequence[i]):
            return arrSequence[:i]

### EXERCÍCIO 1
def shellSort(arr, size):
    shell = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
    knuth = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
    ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]
    listasequencias = [shell, knuth, ciura]
    listanomes = ['SHELL', 'KNUTH', 'CIURA']
    arrcopy = arr[:]
    with open('saida1.txt', 'a') as arq:
        for k in range(len(listasequencias)):
            arr = arrcopy[:]
            sequencia = ChoosenSequence(arr, listasequencias[k]) #vetor com a sequência atual         
            h = len(sequencia) -1            
            originalsqnc = f'{arr}'.replace('[', '').replace(']', '').replace(',', '') + f' SEQ={listanomes[k]}'            
            arq.write(originalsqnc + '\n') #Escreve o vetor original no arq de saída, indicando a sequência utlizada
            gap = sequencia[h]
            while(h!= -1): 
                for i in range(gap, size):
                    temp = arr[i]
                    j = i
                    while j >= gap and temp < arr[j-gap]:
                        arr[j] = arr[j-gap]
                        j -= gap
                    arr[j] = temp
                linhaatual = (f'{arr}'.replace('[', '').replace(']', '').replace(',', '') + f' INCR={gap}')
                arq.write(linhaatual + '\n') #Escreve o vetor modificado ao final de cada etapa com o incremento(gap) atual
                h -=1
                gap = sequencia[h]


### EXERCÍCIO 2
def shellSort2(arr, size):    
    shell = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
    knuth = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
    ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]
    listasequencias = [shell, knuth, ciura]
    listanomes = ['SHELL', 'KNUTH', 'CIURA']
    arrcopy = arr[:]     
    processador = '2.50 GHz 6-Core Intel Core i5 12400F '  #Dados do processador onde rodaram os testes
    with open('saida2.txt', 'a') as arq:
        
        for k in range(len(listasequencias)):
            arr = arrcopy[:]
            sequencia = ChoosenSequence(arr, listasequencias[k]) #vetor com a sequência atual         
            h = len(sequencia) -1  
            inicio = time.perf_counter() # começa a conometrar o tempo
            gap = sequencia[h]
            while(h!= -1): 
                for i in range(gap, size):
                    temp = arr[i]                    
                    j = i
                    while j >= gap and temp < arr[j-gap]:
                        arr[j] = arr[j-gap]
                        j -= gap
                    arr[j] = temp                
                h -=1
                gap = sequencia[h]
            fim = time.perf_counter() # termina de conometrar
            tempototal = (fim - inicio)*1000 #converte para milisegundos
            tempototal = format(tempototal, '.6f')
            linhaatual = f'{listanomes[k]},{size},{tempototal}, {processador}' + '\n'
            arq.write(linhaatual)
        



def TestedeEscala(arq='entrada2.txt'):
    with open ('saida2.txt', 'w'):
        pass  #limpa o arquivo de saída2

    with open(arq, 'r') as arq2:
        for linha in arq2:
            linha = linha.split()
            linha = list(map(int,linha)) #transforma a linha do arquivo de entrada em um vetor com os números
            tamanho = linha[0]
            linha.remove(linha[0]) #remove o primeiro elemento do vetor q indica o tamanho do vetor
            shellSort2(linha, tamanho)

######## main ##########


if len(sys.argv) == 2:
    arquivo_entrada = sys.argv[1]   #Pega o primeiro argumento da linha de comando pra ser o nome do arquivo de entrada, senão por padrão é o arquivo entrada1.txt
else:
    arquivo_entrada = 'entrada1.txt'    

### EXERCÍCIO 1
with open ('saida1.txt', 'w'):
    pass  #limpa o arquivo de saída1
with open(arquivo_entrada, 'r') as arq:
    for linha in arq:
        linha = linha.split()
        linha = list(map(int,linha)) #transforma a linha do arquivo de entrada em um vetor com os números
        tamanho = linha[0]
        linha.remove(linha[0]) #remove o primeiro elemento do vetor q indica o tamanho do vetor
        shellSort(linha, tamanho)


### EXERCÍCIO 2

#TestedeEscala('entrada2.txt')      ### Chamada do Teste de Escala, tem como argumento opcional o nome do arquivo a ser testado, por padrão é 
                                    ### arquivo 'entrada2.txt', e grava o resultado no arquivo 'saida2.txt'