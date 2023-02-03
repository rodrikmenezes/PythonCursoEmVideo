'''
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

# Limpar terminal 
import os; os.system('cls')

# Entrada
n = input('Informe um número entre 0 e 9999: ')

# Cálculo
if int(n) // 1000 > 0:
    print('\nMilhar = {}\nCentena = {}\nDezena = {}\nUnidade = {}'.format(n[0], n[1],n[2], n[3]))
elif int(n) // 1000 == 0 and int(n) // 100 > 0:
    print('\nCentena = {}\nDezena = {}\nUnidade = {}'.format(n[0], n[1], n[2]))
elif int(n) // 100 == 0 and int(n) // 10 > 0:
    print('\nDezena = {}\nUnidade = {}'.format(n[0], n[1]))
else:
    print('\nUnidade = {}'.format(n))
