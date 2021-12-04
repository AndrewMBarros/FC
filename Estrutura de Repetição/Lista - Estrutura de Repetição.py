1 - Faça um programa que peça uma nota, entre zero e dez.

    Mostre uma mensagem caso o valor seja inválido e
    continue pedindo até que o usuário informe um valor válido.

def notas ():
    nota = int(input('Digite uma nota enre 0 e 10: '))   

    return nota

def mensagem (nota):
    while True:
        if (nota > 10 or nota < 0):
            print(f'Erro e digite novamente! ')

            nota = int(input('Digite corretamente: '))
        else:

            break
    print(f'Você digitou corretamente')    
    return 

        
nota = notas()
mensagem (nota)

# ------------------------------------------------- -------------------------------------------------- ---------- #
2 - Faça um programa que leia um nome de usuário
    e a sua senha e não aceite a senha igual ao nome do usuário,
    mostrando uma mensagem de erro e voltando a pedir as informações

def leitura ():
    #leia um nome de usuário
    #e a sua senha

    nome = str(input('Digite o nome do usuário: '))
    senha = str(input('Digite a senha do usuário: '))

    return nome, senha

def analise (senha, nome):
    while True:

        #não aceite a senha igual ao nome do usuário,
        if senha == nome:

            #mostrando uma mensagem de erro
            print(f'A senha é o mesmo nome do usuário. Digite novamente!')

            #voltando a pedir as informações
            nome = str(input('Digite o nome do usuário: '))
            senha = str(input('Digite a senha do usuário: '))
            
        else:
            break
    print(f'Você digitou corretamente. A senha é diferente do usuário!')

    return

nome, senha = leitura ()
analise (senha, nome)

# ------------------------------------------------- -------------------------------------------------- ---------- #
6 - Faça um programa que imprima na tela os números de 1 a 20,
    um abaixo do outro.
    Depois modifique o programa para que ele
    mostre os números um ao lado do outro

#um abaixo do outro
def numeros ():
    print(f'\nO números um abaixo do outro são:')
    for i in  range (1,21):
        print (i)
        
#um do lado do outro
    print(f'\nO números um ao lado do outro são:')
    for i in  range (1,21):
        print(i, end = ' ')
    return

numeros ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
7 - Faça um programa que leia 5 números e informe o maior número


def numeros ():
    maior = 0
    for i in range (1,6):
        numero = float(input('Digite um número: '))

        if numero > maior:
            maior = numero
    print (f' O maior número digitado foi: {maior}')

    return numero
numero = numeros ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
8 - Faça um programa que leia 5 números e
    informe a soma e a média dos números

def numeros ():
    soma = 0

    for i in range (1,6):
        numero = float(input('Digite um número: '))
        soma += numero 
        media = soma /5
        
    print(f' A soma dos números é {soma} e a média é {media}')
    return numero

numero = numeros ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
9 - Faça um programa que imprima na tela apenas os números ímpares
    entre 1 e 50.

def numeros():

    print(f'\nO números ímpares entre 1 e 50 são:')
    for i in range (1,51,2):
        print(i)
    return

numeros ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
