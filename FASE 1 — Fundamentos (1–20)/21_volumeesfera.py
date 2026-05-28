"""
faça um algoritmo para calcular o volume de uma esferade raio R definida pelo usuário. O volume de uma esfera é dado por V = 4/3 * pi * R^3, onde pi é aproximadamente 3.14.
"""

import math 
raio = float(input("Digite o valor do raio da esfera:"))

if raio < 0:
    print("O valor do raio deve ser positivo.")
else:
    volume = (4/3) * math.pi * (raio**3)
    print(f"O volume da esfera é: {volume:.2f}")