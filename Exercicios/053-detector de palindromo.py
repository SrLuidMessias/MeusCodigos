# Crie um programa que leia uma frase qualquer e diga se ela é 
# um palíndromo, desconsiderando os espaços.
frase=str(input('digite:')).lower().strip()
txt=frase.split()
junto=''.join(txt)
inverso='' # - para dizer ao python que tem uma variavel que vai ser usada
for letra in range(len(junto)-1, -1, -1):# --- aqui inverte a frase     
    inverso=inverso + junto[letra]       # --- aqui inverte a frase
if inverso == junto:
    print('É um palíndromo!')
else:
    print('NÃO é um palíndromo!')
# A função len() retorna um número 
# (o tamanho da palavra), então len()-1
# equivale a posição da última letra, 
# que será o início da ordem reversa

