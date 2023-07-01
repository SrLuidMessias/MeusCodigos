'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
from emoji import emojize
colocados=('palmeiras','internacional','fluminence','corithians','flamengo',
'athletico PR','atletico MG','fortaleza','são paulo','botafogo','america','santos','goias',
'red bull bragantino','coritiba','cuiaba','ceara','atletico GO','avai','juventude')
print(emojize(':man_bouncing_ball:'*20))
print('\033[32;41mListas de times brasileiros\033[m')
print(emojize(':man_bouncing_ball:'*20))
print(f'Os 5 primeiros são {colocados[0:5]}')
print(emojize(':soccer_ball:'* 20))
print(f'Os 4 últimos são {colocados[-4:]}')
print(emojize(':soccer_ball:'* 20))
print('times em ordem alfabética:',sorted(colocados))
print(emojize(':soccer_ball:'* 20))
# Se rodar o programa com aspas simples ('') vai dar erro, pois já tem uma aspa do formatado
# Vc pode usar o format ou aspas duplas("")
print(f'flamengo se encontra na {colocados.index("flamengo")+1}ª posição')





