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

# ------------------------------------------------- -------------------------------------------------- ---------- #
7 - Elabore um programa para criptografar e decriptografar
    uma mensagem seguindo o seguinte padrão:
    Somar 2 ao código ascci de cada letra ou caracter.
    Exibir o texto lido, criptografado e decriptografado.
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas


def leitura ():
    frase = str(input('Digite uma frase: '))
    return frase

def analise (frase):
    novapalavra = ''
    for i in frase:
        novapalavra += chr(ord(i)-1)


    print(f'A frase é {frase}')
    print(f'Ela criptografada é: {novapalavra}')

    return novapalavra

frase = leitura ()
analise (frase)

# ------------------------------------------------- -------------------------------------------------- ---------- #
10 - Dado uma string com uma frase informada pelo usuário
    (incluindo espaços em branco), conte:
    quantos espaços em branco existem na frase.

    quantas vezes aparecem as vogais
    (independentemente se são maiúsculas ou minúsculas)
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def palavras ():
    palavra = str(input('Digite uma palavra: '))

    return palavra

def analise (palavra):
    
    print ('A quantidade de espaço branco é {}'.format(palavra.count(' ')))
    
    print ('a letra a aparece {} vezes'.format(palavra.lower().count('a')))
    print ('a letra e aparece {} vezes'.format(palavra.lower().count('e')))
    print ('a letra i aparece {} vezes'.format(palavra.lower().count('i')))
    print ('a letra o aparece {} vezes'.format(palavra.lower().count('o')))
    print ('a letra u aparece {} vezes'.format(palavra.lower().count('u')))

    
    return

palavra = palavras()
analise (palavra)

# ------------------------------------------------- -------------------------------------------------- ---------- #
12 - Elabore um programa que leia uma quantidade indeterminada de nomes.
    Exiba quantas vezes o nome
    joão aparece independente de sua posição no nome.
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def leitura():
    contador = 0
    while True:
        try:
            nome = str(input('Digite um nome ou sair para sair: ')).lower()
            if nome.isnumeric():
                raise
            elif 'joao' in nome:
                contador += 1
            elif nome == 'sair': break
        except:
            print('Digite corretamete!')
    return contador

def analise(nome):
    print(f'A Quantidade de vezes que o nome joao apareceu foi {contador}')

    return contador

contador = leitura()
analise(contador)

# ------------------------------------------------- -------------------------------------------------- ---------- #
15 - Faça um programa que leia um número de telefone,
    e corrija o número no caso deste conter somente 7 dígitos,
    acrescentando o '3' na frente.

    O usuário pode informar o número com ou sem o traço separador.
    Exibir o numero do telefone formatado.(ver exemplo)
    Exemplo:
    Valida e corrige número de telefone
    Telefone: 461-0133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133

    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def leitura ():
    numero = str(input('Digite o número do telefone de 8 algarismos: '))
    return numero

def analise (numero):
    if len(numero) < 8:
        
        print('Telefone: {}'.format(numero))
        print('o numero digitado possui {} algarismos. Vou acrescentar o digito três na frente.'.format(len(numero)))
        print(f'O numero corigido sem formatação é 3{numero}')
        print('o número corrigido com formatação é 3{}{}{}'.format(numero [0:4], '-', numero[4:8]))
    else:
        print('Telefone: {}'.format(numero))
        print('o numero digitado possui {} algarismos. Está correto!'.format(len(numero)))
        print('o número sem correção, mas com formatação é {}{}{}'.format(numero [0:4], '-', numero[4:8]))

    return

numero = leitura()
analise (numero)

# ------------------------------------------------- -------------------------------------------------- ---------- #
17 - Elabore um programa para criptografar e
    depois decriptografar uma mensagem seguindo o seguinte 
    padrão: Para criptografar:Subtrair 1 ao código ascci de cada letra ou caracter.
    Exibir o texto lido, criptografado e decriptografado.
    O programa deverá ser modularizado com pelo menos 2 funções
    Todas as respostas devem vir com mensagens explicativas

def leitura ():
    try:
        frase = str(input('Digite uma string: '))
        return frase

    except:
        print ('Digite corretamente')

    return

def analise (frase):
    resultado = ''
    for i in frase:
        resultado += chr(ord(i)-1)

    print(f'A string é: {frase}')
    print(f'O resultado é: {resultado}')


    return resultado

frase = leitura ()
analise (frase)

# ------------------------------------------------- -------------------------------------------------- ---------- #
