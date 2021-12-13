 1 - Elabore um programa que leia o vetor A com 5 valores inteiros.
    Determine umvetor com a seguinte lei de formação: Os termos de ordem
        impar de A são 
    multiplicados por 3 Os termos de ordem par de A são multiplicados por 2

def inicio ():
    vetor = []
    return vetor

def analise (vetor):
    for pos in range (0,5):
        vetor.append(int(input('Digite um número: ')))
        if pos % 2 == 0:
            vetor [pos] = vetor [pos] * 2
        if pos % 2 == 1:
            vetor [pos] = vetor [pos] * 3
    print ('O vetor é: ', vetor)
    
    return analise

vetor = inicio ()
analise (vetor)

# ------------------------------------------------- -------------------------------------------------- ---------- #
2 - Elabore um programa que leia dois vetores e
    determine o número de elementos
    em comum entre 2 listas dadas como parâmetro. Exemplo: L1=[1,2,3,4,5] e
    L2=[2,4]tem 2 elementos em comum.

def inicio ():
    vet1 = []
    vet2 = []
    vet3 = []
    cont = 0

    return vet1, vet2, vet3, cont

def analise (vet1, vet2, vet3, cont):
    n = int(input('Adicione um valor para o vetor 1 (-1 para sair): '))
    while n != -1:
        vet1.append(n)
        n = int(input('Adicione um valor para o vetor 1 (-1 para sair): '))
    print (vet1)

    n = int(input('Adicione um valor para o vetor 2 (-1 para sair): '))
    while n != -1:
        vet2.append(n)
        n = int(input('Adicione um valor para o vetor 1 (-1 para sair): '))
    print (vet1)

    for i in range (0, len(vet1)):
        for j in range (0, len(vet2)):
            if vet1[i] == vet2[j]:
                cont += 1
    print(f'O numero de elementos em comum é {cont}')

    return n

vet1, vet2, vet3, cont = inicio ()
analise (vet1, vet2, vet3, cont)

# ------------------------------------------------- -------------------------------------------------- ---------- #
8 -  Elabore um programa que leia uma matriz quadrada de tamanho mxm
    elementos inteiros e, verifique se a matriz ´e identidade.
    Imprimir a matriz lida
    sob a forma de tabela e o resultado obtido.

def inicio ():
    flag = 0
    tamanho = int(input('Digite o tamanho da matriz quadrada: '))
    matriz1 = []

    return flag, tamanho, matriz1

def analise (flag, tamanho, matriz1):
    for i in range (0, tamanho):
        matriz1.append(0)
        matriz1[i] = []
        for j in range (0, tamanho):
            elem = int(input(f'Digite o elemento da linha {i+1} e coluna {j+1}: '))
            matriz1[i].append(elem)

    for linha in range(0,tamanho):
        for coluna in range (0, tamanho):
            if ((linha == coluna) and (matriz1[linha][coluna] != 1)):
                flag = -1
            elif ((linha != coluna) and (matriz1[linha][coluna] != 0)):
                flag = -1

    for linha in range(0, tamanho):
        for coluna in range(0,tamanho):
            print(f'{matriz1[linha][coluna]}', end = " ")
        print ()

    if flag == 0:
        print('A matriz é identidade')
    else:
        print('A matriz não é identidade')

    return elem

flag, tamanho, matriz1 = inicio ()
analise (flag, tamanho, matriz1)

