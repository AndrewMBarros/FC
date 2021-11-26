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
10 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def periodo ():
    turno = str(input('Digite o turno o qual você estuda: '))

    return turno

def comparacao (turno):
    if turno == 'm':
        print(f' Bom dia! Você estuda no turno {turno}')
    elif turno == 'v':
        print (f' Boa tarde! Você estuda no turno {turno}')
    elif turno == 'n':
        print(f' Boa noite! Você estuda no turno {turno}')
    else:
        print(f'Valor inválido! Escolha um turno corretamente')

turno = periodo()
comparacao (turno)

# ------------------------------------------------- -------------------------------------------------- ---------- #
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
    lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
            o salário antes do reajuste;
            o percentual de aumento aplicado;
            o valor do aumento;
            o novo salário, após o aumento.

def dinheiro ():
    salario = float(input('Digite o seu salário: '))

    return salario

def reajuste (salario):
    if salario <= 280.0:
        novo20sal = (salario * 0.20) + salario
        print(f'O novo salário é de {novo20sal}')

    elif 280 < salario < 700.0:
        novo15sal = (salario * 0.15) + salario
        print(f'O novo salário é de {novo15sal}')

    elif 700 < salario < 1500.0:
        novo10sal = (salario * 0.10) + salario
        print(f'O novo salário é de {novo10sal}')

    elif salario <= 1500:
        novo5sal = (salario * 0.05) + salario
        print (f'O novo salario é de {novo5sal}')
            

salario = dinheiro ()
reajuste (salario)

# ------------------------------------------------- -------------------------------------------------- ---------- #
13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def calendario ():
    dia = int(input('Digite um dia: '))

    return dia

def verificacao (dia):

    if dia == 1:
        print(f'Você digitou o dia {dia} que equivale ao Domingo')
    elif dia == 2:
        print(f'Você digitou o dia {dia} que equivale a Segunda Feira')
    elif dia == 3:
        print(f'Você digitou o dia {dia} que equivale a Terça Feira')
    elif dia == 4:
        print(f'Você digitou o dia {dia} que equivale a Quarta Feira')
    elif dia == 5:
        print(f'Você digitou o dia {dia} que equivale a Quinta Feira')
    elif dia == 6:
        print(f'Você digitou o dia {dia} que equivale a Sexta Feira')
    elif dia == 7:
        print(f'Você digitou o dia {dia} que equivale ao Sábado ')
    else:
        print(f'Você digitou o dia {dia} que está errado')

dia = calendario ()
verificacao (dia)

# ------------------------------------------------- -------------------------------------------------- ---------- #
14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
    e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0        A
    Entre 7.5 e 9.0         B
    Entre 6.0 e 7.5         C
    Entre 4.0 e 6.0         D
    Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def notas ():
    nota1 = float(input('Digite a sua primeira nota: '))
    nota2 = float(input('Digite a sua segunda nota: '))
    media = (nota1 + nota2) / 2 
    return nota1, nota2, media 

def atribuicao (media):
    if 9 <= media <= 10.0:
        print(f'O conceito é A e a sua média é {media}, logo você está Aprovado')
    elif 7.5 <= media < 9.0:
        print(f'O conceito é B e a sua média é {media}, logo você está Aprovado')
    elif 6.0 <= media < 7.5:
        print(f'O conceito é C e a sua média é {media}, logo você está Aprovado')
    elif 4.0 <= media < 6.0:
        print(f'O conceito é D e a sua média é {media}, logo você está Reprovado')
    elif 0 <= media < 4.0:
        print(f'O conceito é E e a sua média é {media}, logo você está Reprovado')

nota1,nota2,media = notas()
atribuicao (media)

# ------------------------------------------------- -------------------------------------------------- ---------- #
16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.

    O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
        Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
        Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
        Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
        Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

def raizes ():
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = b**2 - 4 * a * c

    if a == 0:
        print(f' A equação não é do segundo grau')
    

    elif delta < 0:
        print(f' A equação não possui raizes reais')

    elif delta == 0:
        print(f' A equação possui apenas uma raiz real')

    elif delta > 0:
        print(f' A equação possui duas raizes reais')
    return a, b, c, delta

a, b, c, delta = raizes ()

