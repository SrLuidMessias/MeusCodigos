# Crie um programa que leia o nome de uma cidade, diga se ela começa ou não com o nome “SANTO”.

cid=str(input('digite o nome da cidade:')).strip()
print(cid[:5].upper()== 'SANTO')