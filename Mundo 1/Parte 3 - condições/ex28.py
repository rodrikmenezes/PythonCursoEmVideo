"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# Módulos
import random as rd
import time as tm

# Limpar terminal 
import os; os.system('cls')

# Entrada
n = rd.randint(0, 5)
g = int(input('Adivinhe qual foi o número escolhido! (0 <= n <= 5): '))

# Saída
print('\n\033[1;31mPROCESSANDO...\033[0;0m') # configurado para ser colorido
tm.sleep(1)

if g == n:
    print('VC ACERTOU!')
else:
    print('ERROU!, o número correto era {}'.format(n))
