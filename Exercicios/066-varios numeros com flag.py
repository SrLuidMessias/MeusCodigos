'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
s = c = 0
while True:
    n = int(input('Digite um número [999] para parar:'))
    if n == 999:  #<--- para o flag "999" não ser contado, entao o break fica em cima
        break
    c += 1
    s += n
print(f'a soma desses {c} valores foram {s}')






