# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase=str(input('Digite uma frase:')).strip().upper()
print('Totais de letras "A" são:{}'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição:{}'.format(frase.find('A')))
print('A última letra "A" aparece na posição:{}'.format(frase.rfind('A')))