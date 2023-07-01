'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
soma = produtocaros = menorp = cont = 0
barato=''
while True:
    nomep=str(input('Nome do Produto:'))
    preco=int(input('Preço: R$'))
    con = str(input('Quer continuar? [S|N]')).upper()
    cont += 1
    soma += preco
    if preco > 1000:
        produtocaros+= 1
    if cont == 1 or preco < menorp:
        menorp = preco
        barato = nomep#<--- O nome do produto mais barato vai ser mostrado, porque
    if con == 'N':         #está aqui, onde mostra o preço mais barato
        break
print(f'Total da compra foi R${soma:.2f}')
print(f'temos {produtocaros} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${preco:.2f}')