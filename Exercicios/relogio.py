from time import sleep

hora = int(input('HORA (Formato 12h): '))
min = int(input('MIN: '))
seg = int(input('SEG: '))
n = 0
horad = int(input('Digite um horário para o despertador: \n HORA (Formato 12h): '))
mind = int(input('MIN: '))
if hora < 12 and min < 60 and seg < 60:
    while n == 0:
        print('{:2}h : {:2}min : {:2}s'.format(hora, min, seg))
        sleep(1)
        seg+= 1
        if seg > 59:
            seg = 0
            min+= 1
        if min > 59:
            min = 0
            seg = 0
            hora+= 1
        if hora > 11:
            hora = 0
            seg  = 0
            min  = 0
        if hora == horad and min == mind:
            print('ALARME!!!!')
            horad=0
            mind=0
else:
    print('Valores digitados inválidos!')