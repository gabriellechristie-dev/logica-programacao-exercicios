"""
Construa um programa para calcular as raizes de uma equação do segundo grau(ax^2 + bx + c = 0), sendo que o valores a,b,c são fornecidos pelo usário(considere que a equação possui duas raizes reais).
"""

import math

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raízes reais.")
    exit()
else:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)

print(f"As raízes da equação são: {raiz1} e {raiz2}")
