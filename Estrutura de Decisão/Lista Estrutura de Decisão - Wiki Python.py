1 - Faça um Programa que peça dois números e imprima o maior deles.

def leitura ():

    #peça dois número

    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    return numero1, numero2

def comparaeimprime (numero1,numero2):
    if numero1 > numero2:
        maior = numero1
    else:
        maior = numero2
        
    #imprima o maior deles
    print(f'O maior número entre eles é: {maior}')
    return maior

numero1, numero2 = leitura ()
maior = comparaeimprime (numero1, numero2)

# ------------------------------------------------- -------------------------------------------------- ---------- #
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


def numeroqualquer ():

    #peça um valor
    numero = float(input('Digite um número qualquer: '))

    return numero
    
def comparacao (numero):

    #mostre na tela se o valor é positivo ou negativo

    #foi considerado que 0 não é negativo e nem positivo

    if numero > 0:
        print(f'Esse número é positivo')
    if numero < 0: 
        print(f'Esse número é negativo')
    return 0

numero = numeroqualquer ()
numero = comparacao (numero)

# ------------------------------------------------- -------------------------------------------------- ---------- #
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def letraqualquer ():
    letra = str(input('Digite uma letra: '))

    return letra

def sexo (letra):
    #verifique se uma letra digitada é "F" ou "M"

    #Conforme a letra escrever: F - Feminino
    if letra == 'f':
        print(f'Essa letra que você digitou {letra} corresponde ao sexo feminino')

    #M - Masculino
    else:
        if letra == 'm':
            print(f'Essa letra que você digitou {letra} corresponde ao sexo masculino')

        #Sexo Inválido.
        else:
            print(f'Essa letra corresponde a um sexo inválido')
    return

letra = letraqualquer()
letra = sexo(letra)

# ------------------------------------------------- -------------------------------------------------- ---------- #
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def letradigitada ():
    letra = str(input('Digite uma letra: '))

    return letra


def verificacao (letra):

    #verifique se uma letra digitada é vogal 
    if letra == 'a':
        print(f'Essa letra que você digitou {letra} corresponde a uma vogal')
    elif letra == 'e': 
        print(f'Essa letra que você digitou {letra} corresponde a uma vogal')
    elif letra == 'i':
        print(f'Essa letra que você digitou {letra} corresponde a uma vogal')
    elif letra == 'o': 
        print(f'Essa letra que você digitou {letra} corresponde a uma vogal')
    elif letra == 'u':
        print(f'Essa letra que você digitou {letra} corresponde a uma vogal')

    #ou consoante
    else:
        print(f'Essa letra que você digitou {letra} corresponde a uma consoante')
    return 

letra = letradigitada ()
letra = verificacao (letra)

# ------------------------------------------------- -------------------------------------------------- ---------- #
5 - Faça um programa para a leitura de duas notas parciais de um aluno.
    O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.


def notas ():
    #Faça um programa para a leitura de duas notas parciais de um aluno.

    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    
    return nota1, nota2


def mediadasnotas( nota1, nota2 ):
    #O programa deve calcular a média alcançada por aluno e apresentar:

    media = (nota1 + nota2) /2 

    #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    if 10.0 > media >= 7.0:
        print (f'O aluno com média {media} está Aprovado')

    #A mensagem "Reprovado", se a média for menor do que sete;
    elif media < 7.0:
        print(f'O aluno com média {media} está Reprovado')

    #A mensagem "Aprovado com Distinção", se a média for igual a dez.
    elif media == 10.0:
        print(f'O aluno com média {media} está Aprovado com Distinção')

    return media

nota1, nota2 = notas()
media = mediadasnotas( nota1, nota2 )

# ------------------------------------------------- -------------------------------------------------- ---------- #
6 - Faça um Programa que leia três números e mostre o maior deles

def numeros():

    #leia três números

    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    numero3 = float(input('Digite o terceiro número: '))

    return numero1, numero2, numero3


def comparacao(numero1,numero2,numero3):

    #mostre o maior deles.

    if (numero1 > numero2) and (numero1 > numero3):
        print(f'O número {numero1} é maior deles') 

    elif (numero2 > numero3) and (numero2 >  numero1):
        print(f'O número {numero2} é maior deles')

    elif (numero3 > numero1) and (numero3 >numero2):
        print(f'O número {numero3} é maior deles')
    else:
        print('Os numeros são iguais, logo não há maior!')
        
numero1, numero2, numero3 = numeros()
comparacao (numero1,numero2,numero3)

# ------------------------------------------------- -------------------------------------------------- ---------- #
7 - Faça um Programa que leia três números e mostre o maior e o menor deles

def numeros ():
    
    #leia três números 
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    numero3 = float(input('Digite o terceiro número: '))

    return numero1, numero2, numero3

#mostre o maior 
def maior (numero1, numero2, numero3):
    
    if (numero1> numero2) and (numero1 > numero3):
        print(f'O primeiro número escolhido {numero1} é o maior de todos')
    elif (numero2 > numero3) and (numero2 > numero1):
        print(f'O segundo número escolhido {numero2} é o maior de todos')
    elif (numero3 > numero1) and (numero3 > numero2):
        print (f'O terceiro número escolhido {numero3} é o maior de todos')

#mostre o menor deles
def menor (numero1, numero2, numero3):
    if (numero1 < numero2) and (numero1 < numero3):
        print(f'O primeiro número escolhido {numero1} é o menor de todos')
    elif (numero2 < numero3) and (numero2 < numero1):
        print(f'O segundo número escolhido {numero2} é o menor de todos')
    elif (numero3 < numero1) and (numero3 < numero2):
        print(f'O terceiro número escolhido {numero3} é o menor de toodos')

    #caso os tres forem iguais
    else:
        print('Os numeros são iguais, logo não há maior e nem menor!')


numero1, numero2, numero3 = numeros ()
maior (numero1, numero2, numero3)
menor (numero1, numero2, numero3)

# ------------------------------------------------- -------------------------------------------------- ---------- #
8 - Faça um programa que pergunte o preço de três produtos e
    informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato

def produtos ():

    #pergunte o preço de três produtos
    produto1 = float(input('Digite o preço do Primeiro Produto: '))
    produto2 = float(input('Digite o preço do Segundo Produto: '))
    produto3 = float(input('Digite o preço do Terceiro Produto: '))

    return produto1, produto2, produto3

def comparacao (roduto1, produto2, produto3):

    #sabendo que a decisão é sempre pelo mais barato
    if (produto1 < produto2) and (produto1 < produto3):
        print(f'O preço do produto mais barato custa {produto1} e por isso foi o escolhido')

    elif (produto2 < produto3) and (produto2 < produto1):
        print(f'O preço do produto mais barato custa {produto2} e por isso foi o escolhido')

    elif (produto3 < produto1) and (produto3 < produto1):
        print(f'O preço do produto mais barato custa {produto3} e por isso foi o escolhido')

produto1, produto2, produto3 = produtos ()
comparacao (produto1, produto2, produto3)

# ------------------------------------------------- -------------------------------------------------- ---------- #
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

def numeros ():
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    numero3 = float(input('Digite o terceiro número: '))

    return numero1, numero2, numero3

def ordem (numero1, numero2, numero3):
    if (numero1 > numero2) and (numero1 > numero3):
        print(f'O maior número é o {numero1} seguido pelo {numero2} e seguido pelo {numero3}')
    elif (numero2 > numero3) and (numero2 > numero1):
        print(f'O maior número é o {numero2} seguido pelo {numero1} e seguido pelo {numero3}')
    elif (numero3 > numero1) and (numero3 > numero2):
        print(f'O maior número é o {numero3} seguido pelo {numero2} e seguido pelo {numero1}')

numero1, numero2, numero3 = numeros()
ordem (numero1, numero2, numero3)

# ------------------------------------------------- -------------------------------------------------- ---------- #
