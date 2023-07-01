from time import sleep
print('-°'*15)
start=input('Press [ENTER]')
print('-°'*15)
t1=0
t2=1
print('{}-{}'.format(t1, t2),end='')
count=3
while count <= 3:
    t3 = t1 + t2
    print('-{}'.format(t3),end='')
    t1 = t2
    t2 = t3
    sleep(1)
    count += 0