3 - Faça um programa que permita ao usuário digitar o seu nome
    e em seguida mostre o nome do usuário de trás para frente
    utilizando somente letras maiúsculas. Dica: lembre−se que ao
    informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def leitura ():
    palavra = str(input('Digite uma palavra: ')).strip().upper()
    return

def palindromo (palavra):
    palavraoriginal = palavra
    palavra = palavra.lower()
    novapalavra = ''

    if ' ' in palavra:
        palavra = palavra.replace(' ', '')

    for i in range (-1, -len(palavra)-1, -1):
        novapalavra += palavra [i]

    print (novapalavra)
    if palavra == novapalavra:
        return (f'{palavraoriginal} é palindromo').upper()
    else:
        return(f'{palavraoriginal} não é palindromo').upper()

frase = input('Escreva uma frase: ')

print(palindromo(frase))

# ------------------------------------------------- -------------------------------------------------- ---------- #
4 - Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
    do usuário e imprima a data com o nome do mês por extenso.
    Data de Nascimento: 29/10/1973
    Você nasceu em 29 de Outubro de 1973.
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def leitura ():
    dia = str(input('Digite o dia do seu nascimento: '))
    mes = str(input('Digite o mês do seu nascimento: '))
    ano = str(input('Digite o ano do seu nascimento: '))

    return dia, mes, ano

def analise(dia, mes, ano):
    mes = float(mes)
    if len(ano) < 4:
        print('Digite o ano corretamente!')
    if mes > 30:
        print('O mes só tem 30 dias')

    else:
        if mes == 1:
            print(f'Sua data de nascimento é {dia} de Janeiro de {ano}')
        elif mes == 2:
            print(f'Sua data de nascimento é {dia} de Fevereiro de {ano}')
        elif mes == 3:
            print(f'Sua data de nascimento é {dia} de Março de {ano}')
        elif mes == 4:
            print(f'Sua data de nascimento é {dia} de Abril de {ano}')
        elif mes == 5:
            print(f'Sua data de nascimento é {dia} de Maio de {ano}')
        elif mes == 6:
            print(f'Sua data de nascimento é {dia} de Junho de {ano}')
        elif mes == 7:
            print(f'Sua data de nascimento é {dia} de Julho de {ano}')
        elif mes == 8:
            print(f'Sua data de nascimento é {dia} de Agosto de {ano}')
        elif mes == 9:
            print(f'Sua data de nascimento é {dia} de Setembro de {ano}')
        elif mes == 10:
            print(f'Sua data de nascimento é {dia} de Outubro de {ano}')
        elif mes == 11:
            print(f'Sua data de nascimento é {dia} de Novembro de {ano}')
        else:
            print(f'Sua data de nascimento é {dia} de Dezembro de {ano}')
    return

dia, mes, ano = leitura ()
analise (dia, mes, ano)

# ------------------------------------------------- -------------------------------------------------- ---------- #
 6- Escreva um programa em Python que conte a quantidade de vogais
    e de consoantes de uma string.
    Não pode usar count.
    O usuário pode usar letras maiúsculas e/ou minúsculas
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def leitura ():
    palavra  = str(input('Digite uma palavra: '))
    return palavra

def analise (palavra):
    vogal = 0
    consoante = 0
    dado = palavra.split ()
    dados1 = dado [0]
    for i in dados1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vogal += 1
        else:
            consoante +=1
    return dados1, vogal, consoante

def imprimir (dados1, vogal, consoante):
    print(f'a string {dados1} contem {consoante} consontes e {vogal} vogais')
    return

palavra = leitura ()
dados1, vogal, consoante = analise (palavra)
imprimir (dados1, vogal, consoante)
