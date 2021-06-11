""" 
Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada. 
"""

# Entrada de dados 
n = int(input('Digite um número inteiro para ver sua tabuada: '))

# Cálculo e print
for m in range(1, 10):
    # Print 1
    # print('{} x {} = {}'.format(n, m, n*m))
    
    # Print 2
    print(f'{n} x {m} = {n*m}')