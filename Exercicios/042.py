# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
print('digite os segmentos')
s1 = float(input('Primeiro segmento :'))
s2 = float(input('Segundo segmento :'))
s3 = float(input('Terceiro segmento :'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os segmentos acima PODEM FORMAR um triângulo ', end='')
    if s1 == s2 == s3:                  # condição aninhada, é como se fosse                                       
        print('EQUILÁTERO!')            # um ninho dentro de um ninho...etc
    elif s1 != s2 != s3 != s1:          #TUDO ISSO É POSSIVÉL, NÃO SE ESQUEÇA LUID!!!!
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('os segmentos acima NÃO PODEM FORMAR um triângulo ')
