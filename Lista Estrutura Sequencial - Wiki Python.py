1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def mensagem ():
print ('Alo mundo')

texto = str (input ('Alo mundo'))
mensagem ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
2. Faça um Programa que peça um número e então mostre a mensagem O número foi [número].
def numero ():

numero = float(input('Digite um número: '))

print (' O número digitado foi [{}] '.format(numero))

return
numero ()

# ------------------------------------------------- -------------------------------------------------- ---------- #
3 - Faça um Programa que peça dois números e imprima a soma.

def soma (x, y):

s = x + y
return s 
a = int (input ('Número 1:'))
b = int (input ('Número 2:'))
print ('Soma:', soma (a, b))

# ------------------------------------------------- -------------------------------------------------- ---------- #
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

mídia de definição (w, x, y, z):
mídia = (w + x + y + z) / 4
mídia de retorno

a = float (input ('Nota 1:'))
b = float (input ('Nota 2:'))
c = float (input ('Nota 3:'))
d = float (input ('Nota 4:' ))

imprimir ('A média é:', media (a, b, c, d))

# ------------------------------------------------- -------------------------------------------------- ---------- #
5. Faça um Programa que converta metros para especificar.

conversor de def (tamanho):
conversor = tamanho * 100
conversor de retorno

metros = float (input ('Digite o tamanho em metros:'))

imprimir ('O tamanho em tamanho é:', conversor (metros))

# ------------------------------------------------- -------------------------------------------------- ---------- #
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#area = pi * r ** 2

def raio (r):
área = 3,14 * (r ** 2)
área de retorno

#considerando pi = 3,14

r = float (input ('Digite o raio:'))

imprimir ('A área é:', raio (r))
