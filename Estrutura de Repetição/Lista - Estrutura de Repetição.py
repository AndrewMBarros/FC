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
13 - Faça um programa que peça dois números, base e expoente,
    calcule e mostre o primeiro número elevado ao segundo número.
    Não utilize a função de potência da linguagem

def numeros ():
    numero1 = float(input('Digite o primeiro número, sendo a base: '))
    numero2 = float(input('Digite o segundo número, sendo o expoente: '))
  
    
    return numero1, numero2

def analise (numero1, numero2):
    while True:
        if (numero1 == 0) and numero2 == 0:
            print(f'Indeterminação! Digite uma base maior que zero!')
            break
        print(f'o primeiro número {numero1} elevado do segundo número {numero2} = {numero1 ** numero2}')

        return
numero1, numero2 = numeros ()
analise (numero1, numero2)

# ------------------------------------------------- -------------------------------------------------- ---------- #
14 - Faça um programa que peça 10 números inteiros,
    calcule e mostre a quantidade de números pares
    e a quantidade de números impares.

def numeros ():
    
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))

    return numero1, numero2

def analise (numero1, numero2):
    par = 0
    impar = 0
    
    for numero in range (numero1, numero2 + 1 ):
        if numero % 2 == 0:
            par +=1
        else:
            impar +=1
    print(f' A quantidade de pares é {par} e a quantidade de impar é {impar}')

numero1, numero2 = numeros ()
analise (numero1, numero2)

# ------------------------------------------------- -------------------------------------------------- ---------- #
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

def leitura ():
    numero = int(input('Digite um número que você deseja calcular o fatoria: '))

    return numero

def fatorial (numero):
    contador = numero
    fatorial = 1

    while contador > 0:
        fatorial *= contador
        contador -= 1

       #analisar esse caso
        #if numero > 0:
        #   print('Digite um número inteiro positivo')'''
       
    print(f' o fatorial de {numero} = {fatorial}')

    return fatorial

numero = leitura ()
fatorial (numero)

# ------------------------------------------------- -------------------------------------------------- ---------- #
21 -Faça um programa que peça um número inteiro
    e determine se ele é ou não um número primo.
    Um número primo é aquele que é
    divisível somente por ele mesmo e por 1.

def leitura ():    
    numero = int(input('Digite um número: '))

    return numero

def primo (numero):
    contador = 0
    for i in range (1, numero +1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        print(f'O número que foi digitado {numero} é primo!')
    else:
        print(f'O número que foi digitado {numero} não é primo!')

numero = leitura ()
primo (numero)

# ------------------------------------------------- -------------------------------------------------- ---------- #
22 - Altere o programa de cálculo dos números primos,
    informando, caso o número não seja primo,
    por quais número ele é divisível.

    programa anterior:

    Faça um programa que peça um número inteiro e
    determine se ele é ou não um número primo.
    Um número primo é aquele que é divisível
    somente por ele mesmo e por 1.

def leitura ():    
    numero = int(input('Digite um número: '))

    return numero

def primo (numero):
    contador = 0
    divisores = 0
    
    for i in range (1, numero +1):
        if numero % i == 0:
            contador += 1
            divisores += 1
    if contador == 2:
        print(f'O número que foi digitado {numero} é primo!  ')

numero = leitura ()
primo (numero)

# ------------------------------------------------- -------------------------------------------------- ---------- #
34 - Os números primos possuem várias aplicações dentro da Computação,
    por exemplo na Criptografia. Um número primo é aquele que é divisível
    apenas por um e por ele mesmo.
    
    Faça um programa que peça um número inteiro
    e determine se ele é ou não um número primo.

def leitura ():    
    numero = int(input('Digite um número: '))

    return numero

def primo (numero):
    contador = 0
    for i in range (1, numero +1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        print(f'O número que foi digitado {numero} é primo!')
    else:
        print(f'O número que foi digitado {numero} não é primo!')

numero = leitura ()
primo (numero)

#caso o número não seja primo, por quais número ele é divisível.
  
    else:
        print(f'O número que foi digitado {numero} não é primo! Ele foi divisivel por {divisores} divisores ')

numero = leitura ()
primo (numero)

# ------------------------------------------------- -------------------------------------------------- ---------- #
50 - Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos

def leitura ():
    numerador  = float(input('Digite o valor para o numerador: '))
    denominador = int(input('Digite o valor para o denominador: '))

    return numerador, denominador

def calculo (numerador, denominador):
    h = 0

    for i in range (1, denominador + 1):
        h += numerador / i
    return h

def imprimir (h):
    print(f'O valor da série é: {h}')
    return

numerador, denominador = leitura()
h = calculo (numerador, denominador)
imprimir (h)

# ------------------------------------------------- -------------------------------------------------- ---------- #
