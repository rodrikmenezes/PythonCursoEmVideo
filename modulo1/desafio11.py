""" 
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e 
a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 
"""

# variáveis
l = float(input('Largura = '))
a = float(input('Altura = '))

# info extra
area = a * l
qtde_tinta = area / 2

# prints
# print(f'\nDimensão da parede: {l} m X {a} m \nÁrea: {area} m² \nQuantidade de tinta: {qtde_tinta} litros')
print('\nDimensão da parede: {} m X {} m \nÁrea: {} m² \nQuantidade de tinta: {} litros'.format(l, a, area, qtde_tinta))

