# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
num=int(input('informe um número:'))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print('analizando o número {}'.format(num))
print('unidade:{}'.format(u))
print('dezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar{}'.format(m))