# Desenvolva um programa que leia o 'nome', 'idade' e 'sexo' de '4 pessoas'. 
# No final do programa, mostre: 'a média de idade do grupo', qual é o 
# 'nome do homem mais velho' e 'quantas mulheres têm menos de 20 anos'.
nome_velho=''
idade_velho=0
idade=0
soma_ida=0
media=0
tot_mulher=0
for c in range(1,5):
    print('\033[36m****{}° pessoa ***** \033[m '.format(c))
    nome=str(input('nome :'))
    idade=int(input('idade :'))
    sexo=str(input('Sexo? (H) ou (M) :')).strip()
    soma_ida += idade
    media = (soma_ida + 0) / c
    if sexo == 'h':
        if idade > idade_velho :
            idade_velho = idade
            nome_velho = nome
    if sexo == 'm':
        if idade < 20:
            tot_mulher += 1
print('A média de idade é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idade_velho, nome_velho))
print('Ao todo são {} mulheres menos de 20 anos'.format(tot_mulher))