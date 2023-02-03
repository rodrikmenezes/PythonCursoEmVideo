"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

# Bibliotecas
import random

# Entrada de dados
alunos = ['Pedro', 'João', 'Carla', 'Helena']

# Escola random
escolhido = random.choice(alunos)

# Print
print('Aluno selecionado: {}'.format(escolhido))