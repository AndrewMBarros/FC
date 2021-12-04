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
