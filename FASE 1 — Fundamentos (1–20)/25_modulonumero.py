"""
Escreva um programa que leia um número e exiba o seu módulo.
"""

numero = float(input("Digite um número:"))

if numero >= 0:
    modulo = numero 
else: 
    modulo = -numero
print(f"O módulo de {numero} é {modulo}.")