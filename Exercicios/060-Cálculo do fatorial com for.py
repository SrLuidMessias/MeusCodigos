'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:'''
n=int(input('digite um número:'))
contador=0
fatorial=1
print('{}!= '.format(n),end='')
for contador in range(n, 0, -1):

    print('{} x'.format(contador),end=' ')
    fatorial *= n
    n -= 1
print('={}'.format(fatorial), end='')