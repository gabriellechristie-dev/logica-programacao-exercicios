"""
Escreva um programa que leia 3 valores e escreva a soma dos 2 maiores.
"""
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 <= n2 and n1 <= n3:
    soma = n2 + n3
elif n2 <= n1 and n2 <= n3:
    soma = n1 + n3
else:
    soma = n1 + n2
print(f"A soma dos 2 maiores números é: {soma}")
