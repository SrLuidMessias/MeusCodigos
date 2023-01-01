cho=input('choice your math operation[/,*,-,+] or f to convert celsius to fahrenheit')
nunb1=int(input('first number'))
nunb2=int(input('secund number'))
r=nunb1
if cho== '/' :
    print(f'nice:{nunb1 / nunb2}')
elif cho == '*':
    print(f'nice:{nunb1 * nunb2}')
elif cho == '-':
    print(f'nice:{nunb1 - nunb2}')
elif cho =='+':
    print(f'ok:{nunb1 + nunb2}')
elif cho =='f':
    print(f'your result is :{(nunb1*9/5)+32}fahrenheit' )

else :
    print('lixo')