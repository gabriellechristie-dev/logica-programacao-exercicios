"""
Escreva um programa que calcula o desconto previdenciário de um funcionário. Dado um
salário, o programa deve retornar o valor do desconto proporcional ao mesmo. O cálculo
segue a regra: o desconto é de 11% do valor do salário, entretanto, o valor máximo de
desconto é 334,29, o que seja menor.
"""
salario = float(input("Digite o salário do funcionário: "))
desconto = salario * 0.11
if desconto > 334.29:
    desconto = 334.29
print(f"O desconto previdenciário é de R$ {desconto:.2f}.") 
