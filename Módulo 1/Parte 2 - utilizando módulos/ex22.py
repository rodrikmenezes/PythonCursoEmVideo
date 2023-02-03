'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
'''

# Limpar terminal 
import os; os.system('cls')

# Entrada
nome = input('Digite seu nome completo: ')

# Operações
maiusculo = nome.upper()
minusculo = nome.lower()
contar = len(nome) - nome.count(' ')
nome_split = nome.split(' ')
contar_prim = len(nome_split[0])

# Print
print('\nMaiúsculo: {}\nMinúsculo: {}\nNúmero de letras: {}\nNúmero de letras (primeiro nome): {}'.format(maiusculo, minusculo, contar, contar_prim))



