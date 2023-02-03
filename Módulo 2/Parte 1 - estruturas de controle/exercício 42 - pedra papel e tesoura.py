"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random

print('Selecione: \n1) PEDRA \n2) PAPEL \n3) TESOURA')
X = int(input('Opção: '))
Y = round(random.randint(1, 3))

# Legenda
legenda = ['PEDRA', 'PAPEL', 'TESOURA']

if X == 1 and Y == 3 or X == 2 and Y == 1 or X == 3 and Y == 2:
    resultado = 'VOCÊ GANHOU!!!'
elif X == Y:
    resultado = 'EMPATE!!!'
else:
    resultado = 'VOCÊ PERDEU!!!'

print('=-'*10)
print('Jogadas:\n\nVocê: {} \nComputador: {} \n\n{}'.format(legenda[X-1], legenda[Y-1], resultado))
print('=-'*10)

