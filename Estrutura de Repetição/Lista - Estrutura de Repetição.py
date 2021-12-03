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

