# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n_i=int(input('Digite um número qualquer:'))
total= 0 # Saber o número de diviseis / nomeado contador
for c in range(1, n_i + 1):
    if n_i % c == 0 :
        print('\033[35m', end=' ')
        total = total + 1
    else:
        print('\033[34m', end=' ')
    print('{} '.format(c), end=' ')

print('\033[m O número {} foi divisivel {} vezes'.format(n_i, total))
if total == 2:
    print('E por isso ele é primo!')
else :
    print('E por isso ele NÃO é primo!')