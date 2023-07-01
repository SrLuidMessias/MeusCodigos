'''Faça um programa que leia 5 valores numéricos e guarde-os em
uma lista.No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.'''
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c} :')))
    ma = max(valores)
    mi = min(valores)
print(f'\nO maior valor é {ma}, e está na posição', end=' ')
for i, v in enumerate(valores):
    if v == ma:
        print(f'{i}...',end=' ')
print(f'\nO menor valor é {mi}, e está na posição',end=' ')
for i, v in enumerate(valores):
    if v == mi:
        print(f'{i}...',end=' ')


