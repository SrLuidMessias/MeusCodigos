'''Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
valor1=int(input('digite uma valor:'))
valor2=int(input('digite mais uma valor:'))
valor3=int(input('digite outro valor:'))
valor4=int(input('digite o ultimo valor'))
tupla=(valor1, valor2, valor3, valor4)
print('Você digitou os valores',end=' ')
for n in tupla:
    print(f'{n}',end=' ')
if 9 in tupla:
    print('\nO valor 9 apareceu', tupla.count(9),'vezes')
else:
    print('\nvalor 9 não encontrado!')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('Valor 3 não encontrado!')
print('Os valores pares digitados foram',end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n,end=' ')
