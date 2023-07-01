'''Crie um programa que tenha uma tupla única com nomes
de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem=('processador i7',2407.86,'placa mãe-revolution',746.46,
          'placa de video-randeon 4870',2382.12,'memória', 1155.96,
          'disco rígido-barracuda',702.00, 'drive blu-ray sony',933.66,
          'gabinete xaser VI', 442.26, 'Sistema operacional', 50.00)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f'{listagem[itens]:.<40}',end='')
    else:
        print(f'R$ {listagem[itens]:.2f}')














