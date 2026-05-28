"""
Faça um algoritmo que calcule e apresente o valor do volume de uma lata de óleo, dado seu raio e sua altura.
"""

# pedir raio da lata 
# pedir altura da lata
# validar entrada
# calcular volume da lata
# mostrar resultado

import math

raio = float(input("Digite o raio da lata:"))
altura = float(input("Digite a altura da lata:"))

if raio <= 0 or altura <=0:
    print("Digite um número válido")

else:
    volume = math.pi * (raio**2)*altura
    print(f"O volume da lata é: {volume:.2f}")