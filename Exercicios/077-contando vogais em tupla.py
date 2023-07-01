'''Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''
palavras = (str(input("Digite uma palavra:")),
            str(input("Digite mais uma palavra:")),
            str(input("A ultima palavra:")))
# "p" retorna todos os valores da tupla e em ordem!
for p in palavras:
    print(f'\nNa palavra {p} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')






