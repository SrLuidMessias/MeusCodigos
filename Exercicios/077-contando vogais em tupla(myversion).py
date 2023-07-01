palavra1 = str(input('Digite uma palavra:'))
palavra2 = str(input('Digite uma palavra:'))
palavra3 = str(input('Digite uma palavra:'))
palavra4 = str(input('Digite uma palavra:'))
palavras = (palavra1, palavra2, palavra3, palavra4)
for p in palavras:
    print(f'\nNa palavra {p.upper()} tem', end='-')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end='-')

