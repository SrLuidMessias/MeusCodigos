'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
totm=toth=idadej=0
print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
while True:
    idade=int(input('idade:'))
    sexo=str(input('sexo [H|M]:')).upper().split()[0]
    print('-'*20)
    conti = str(input('quer continuar?')).upper().split()[0]
    print('-' * 20)
    print('CADASTRE OUTRA PESSOA')
    print('-' * 20)
    if idade >= 18:
        idadej += 1
    if sexo ==  'H':
        toth += 1
    if sexo == 'M' :
        if idade <20:
            totm += 1
    if conti == 'N':
        break
print(f'São {idadej} pessoas maiores de 18 anos')
print(f'Foram {toth} homens cadastrados')
print(f'São {totm} mulheres menos de 20 anos')
