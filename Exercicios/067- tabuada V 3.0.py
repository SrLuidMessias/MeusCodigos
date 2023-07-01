'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''
n = 0
while True:
    n = int(input('Digite um número para a tabuada:'))
    if n < 0:
        break
    print('\033[32m-\033[m'*15)
    for c in range(0, 11):
        print(f'{c} x {n} = {n*c}')
    print('\033[32m-\033[m'*15)

print('fim')



