"""
Escreva um programa que leia 3 números e calcule a média ponderada entre eles.
Considere que o maior número recebe peso 5 e os outros dois recebem peso 2,5.
"""
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    media_ponderada = (n1 * 5 + n2 * 2.5 + n3 * 2.5) / 10
elif n2 >= n1 and n2 >= n3:
    media_ponderada = (n1 * 2.5 + n2 * 5 + n3 * 2.5) / 10
else:
    media_ponderada = (n1 * 2.5 + n2 * 2.5 + n3 * 5) / 10
print(f"A média ponderada é: {media_ponderada}")
