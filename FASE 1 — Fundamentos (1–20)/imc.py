"""
Cuidando da Saúde

Faça um programa para calcular o IMC de uma pessoa, a partir de sua altura e peso. A fórmula para calcular o IMC é: peso / altura2.
"""
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg:"))

imc = peso / altura**2
print(f"Sua altura é {altura} m, seu peso é {peso} Kg e o valor do seu IMC é {imc:.1f}.")