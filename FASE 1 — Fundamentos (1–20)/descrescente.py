"""
escreva um algoritmo que leia três valores inteiros e mostre-os em ordem descrescente.
"""

n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segundo número inteiro:"))
n3 = int(input("Digite o terceiro número inteiro:"))

numeros = [n1,n2,n3]
decrescente = sorted(numeros, reverse = True)

print(f"A ordem decrescente dos números inseridos é: {decrescente}")