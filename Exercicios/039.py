# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou 
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 

##### !!!!!!!!!!!na subtração o maior número deve vim primeiro para ser positivo !!!!!!!!!######


from datetime import date

data_nascimento = int(input('Digite sua data de nascimento :'))
ano_atual = date.today().year
idade_agora = ano_atual - data_nascimento

print('Quem nasceu em {} tem {} em {}.'.format(data_nascimento, idade_agora, ano_atual))

if idade_agora == 18 :
    print('Você precisa se alistar IMEDIATAMENTE!!!')
elif idade_agora < 18:
    idade_jovem = 18 - idade_agora
    ano_alistar = idade_jovem + ano_atual
    print('ainda faltam {} anos para o seu alistamento'.format(idade_jovem))
    print('Você vai se alistar em {}'.format(ano_alistar))
elif idade_agora > 18:
    idade_maior = idade_agora - 18
    ano_alistou = ano_atual - idade_maior
    print('Você deveria ter se alistado há {} anos atrás'.format(idade_maior))
    print('Você se alistou em {}'.format(ano_alistou))