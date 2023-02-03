'''
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

# Entrada
nome = str(input('Digite um nome completo: ')).strip().lower()

# Saída
print("O nome contém 'Silva': {}".format('silva' in nome))