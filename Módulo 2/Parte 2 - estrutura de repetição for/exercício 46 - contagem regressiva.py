"""
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva 
para o estouro de fogos de artifício, indo de 5 até 0, com uma pausa de 1 segundo 
entre eles.
"""

import time


for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print('BOOM!!!')
time.sleep(1)
print('BOOOOOM!!!')
time.sleep(1)
print('BOOOOOOOOOOOM!!!')
time.sleep(1)


