# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for n in range(1, 51):
    if n % 2 == 0:   # sem o if, vai sair só 0 e 1 como resultado
        print(n, end=' ')
print('FIM')
