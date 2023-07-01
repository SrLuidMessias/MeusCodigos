'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.'''
maior = menor = soma = media = c = 0
stop = ''
while stop != 's':
    n = int(input('Digite um número inteiro:'))
    soma += n
    c += 1
    media = soma / c
    if c == 1:     #<----- se não tiver isso não funcinara(pelo menos o menor número no meu caso, o maior funcionou)
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    stop = str(input('deseja parar?[s] ou [ENTER] para continuar :'))
print('Você digitou {} números e a média foi {}'.format(c, media))
print('o menor número foi {} e o maior foi {}'.format(menor, maior))