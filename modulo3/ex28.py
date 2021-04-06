"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# Módulos
import random as rd
import time as tm

# Entrada
n = rd.randint(0, 5)
g = int(input('Adivinhe qual foi o número escolhido! (0 < n < 5): '))

# Saída
print('\nPROCESSANDO...\n')
tm.sleep(2)

if g == n:
    print('VC ACERTOU!')
else:
    print('ERROU!, o número correto era {}'.format(n))