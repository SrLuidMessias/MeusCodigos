### DIFICIL ### DIFICIL ### DIFICIL ### DIFICIL ### DIFICIL ###

''' Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
t=int(input('Primeiro termo:'))
r=int(input('Razão:'))
termo=t
c=1
mais =10
total=0
while mais != 0:
    total += mais
    while c <= total:
        print('{}'.format(termo),end=' ')
        c+=1
        termo += r
    print('pausa')
    mais=int(input('Quantos termos mostrar? :'))
print('Progressão finalizada com {} termos mostrados'.format(total))