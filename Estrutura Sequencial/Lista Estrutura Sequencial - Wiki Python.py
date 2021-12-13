1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

def entrada ():    

    print('Alo mundo')

    return 

entrada ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
2. Faça um Programa que peça um número e então mostre a mensagem O número foi [número].

def numero ():

    numero = float(input('Digite um número: '))

    print (f'O número digitado foi {numero}')

    return

numero ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
3 - Faça um Programa que peça dois números e imprima a soma.

def entrada ():

    a = int(input('Número 1: '))
    b = int(input('Número 2: '))    

    return a, b

def soma (a,b):

    soma = (a + b)

    print (f'O resultado da soma entre o Número 1 e Número 2 é: {soma} ')

    return soma

a, b = entrada ()
soma (a,b)

# ------------------------------------------------- -------------------------------------------------- ---------- #
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def entrada ():

    a = float(input('Nota 1: '))
    b = float(input('Nota 2: '))
    c = float(input('Nota 3: '))
    d = float(input('Nota 4: '))

    return a, b, c, d


def media (a,b,c,d):
    
    media = (a+b+c+d)/4
    
    print(f'\nA média entre as 4 notas é: {media}')

    return media

a, b, c, d = entrada ()
media (a,b,c,d)

# ------------------------------------------------- -------------------------------------------------- ---------- #
5 - Faça um Programa que converta metros para centímetros.


def entrada ():

    metros = float(input('Digite o tamanho em metros: '))
    converter = metros * 100

    print (f'O tamanho em centímetros é: {converter}')

    return

entrada ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#area = pi * r**2


def entrada ():
    r = float(input('Digite o raio do círculo: '))

    return r

def raio (r):
#considerando pi = 3,14
    area = 3.14 * (r ** 2)

    print(f'A área do círculo é: {area}')
    
    return area

r = entrada ()
raio (r)

# ------------------------------------------------- -------------------------------------------------- ---------- #
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def entrada ():
    
    comprimento = float(input('Digite o comprimento do quadrado: '))
    largura = float(input('Digite a largura do quadrado: '))

    return comprimento, largura


def area (comprimento,largura):

    area = comprimento * largura
#mostre o dobro desta área para o usuário.
    dobro = area * 2

    print(f'\nA area do quadrado é {area}')
    print(f'A area do quadrado  ao dobro é: {dobro}')
    
    return area, dobro 

comprimento, largura = entrada ()
area (comprimento,largura)

# ------------------------------------------------- -------------------------------------------------- ---------- #
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def entrada ():
    tempo = float(input('Quantas horas no mês você trabalha? '))
    trabalho = float(input('Quanto você ganha por hora? '))    

    return tempo, trabalho


def hora (trabalho, tempo):
    salario = tempo * trabalho

    print (f'O seu salário é: {salario}')
    return salario

tempo, trabalho = entrada ()
hora (trabalho, tempo)

# ------------------------------------------------- -------------------------------------------------- ---------- #
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9).

def entrada ():
    F = float(input('Digite a temperatura em Farenheit: '))    

    return F


def converter (F):
    c = 5 * ((F-32) / 9)
    
    print(f'A temperatura em Celsius é: {c} ')

    return c

F = entrada ()
converter (F)

# ------------------------------------------------- -------------------------------------------------- ---------- #
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def entrada():
    celsius = float(input('Digite a temperatura em Celsius: '))

    return celsius

def converter (celsius):
    f = 1.8 * celsius + 32

    print (f'A temperatura em Celsius é: {f}')

    return f

celsius = entrada ()
converter (celsius)

# ------------------------------------------------- -------------------------------------------------- ---------- #
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

        o produto do dobro do primeiro com metade do segundo .
        a soma do triplo do primeiro com o terceiro.
        o terceiro elevado ao cubo

def inteiro ():
    inteiro1 = int(input('Digite o Primeiro número inteiro: '))
    inteiro2 = int(input('Digite o Segundo número inteiro: '))
    real = float(input('Digite o Terceiro número sendo ele real: '))    
    
    return inteiro1, inteiro2, real

def analise (inteiro1, inteiro2, real):
    produto = (2 * inteiro1) + (0.5 * inteiro2)
    somaetriplo = (3*inteiro1) + real
    elevado = (real ** 3)

    print(f'O produto do dobro do primeiro com a metade do segundo é: {produto} ')
    print(f'A Soma do triplo do primeiro com o terceiro é: {somaetriplo}')
    print(f'o Terceiro elevado ao cubo é: {elevado} ') 

    return produto, somaetriplo, elevado

inteiro1, inteiro2, real = inteiro ()
analise (inteiro1, inteiro2, real)

# ------------------------------------------------- -------------------------------------------------- ---------- #
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def massa ():
    altura = float(input('Digite a altura de uma pessoa: '))

    return altura

def formula (altura):
    peso = (72.7*altura) - 58

    print(f'O peso da pessoa é {peso} Kg')

    return peso

altura = massa ()
formula (altura)

# ------------------------------------------------- -------------------------------------------------- ---------- #
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7

def inicio ():
    altura = float(input('Digite a altura de uma pessoa: '))

    return altura

def massas (altura):
    pesohomens = (72.7*altura) - 58
    pesomulher = (62.1*altura) - 58

    print(f'O peso da pessoa se ela for homem é {pesohomens} Kg')
    print(f'se ela for mulher o peso é: {pesomulher} kg')

    return pesohomens, pesomulher

altura = inicio ()
massas (altura)

# ------------------------------------------------- -------------------------------------------------- ---------- #
