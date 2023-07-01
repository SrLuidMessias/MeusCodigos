'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('GERADOR DE PA')
print('*'*20)
t=int(input('Primeiro termo:'))
r=int(input('Razão:'))
termo=t
c=1
while c <= 10:
    print('{}'.format(termo),end='-')
    c += 1
    termo += r     #<---- vai fazer o termo seja o termo mais a razão!
print('fim')



''' EX :
a sequência (PA) com o termo 1 e a razão 3 é:
t1=1
r=3
t2 = t1 + r == 1 + 3 = 4
t3 = t2 + r == 4 + 3 = 7 
t4 = t3 + r == 7 + 3 = 10
e ETC...
'''