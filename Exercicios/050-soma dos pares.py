# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma=0
count=0
for c in range(0, 6):
    n=int(input('Digite um número:'))
    if n % 2 == 0:
        soma += n
        count += 1
print('Você informou {} números pares e a soma foi {}'.format(count, soma))