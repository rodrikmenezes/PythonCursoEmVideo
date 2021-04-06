"""
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez
"""

# Entrada
texto = input('Digite uma frase: ').strip().lower()

# Cálculos
n = texto.count('a')
l1 = texto.index('a') + 1
l2 = texto.rindex('a') + 1

# Saída
print("A letra 'a' aparece {} vezes".format(n))
print("Primeira posição: {}".format(l1))
print("Última posição: {}".format(l2))

