""" 
Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles. 
"""

n1 = int(input('n1 = '))
n2 = int(input('n2 = '))

m = n1 + n2

# Print 1
# p = 'A soma vale ' + str(m)
# print(p)

# Print 2
print('A soma entre {} e {} vale {}'.format(n1, n2, m))
