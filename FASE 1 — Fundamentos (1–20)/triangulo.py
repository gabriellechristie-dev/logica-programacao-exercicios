"""
Dado os três lados de um triângulo determinar o perímetro do mesmo. 
"""

# pedir valor dos lados
# validar entrada
# calcular perimetro / p =  a + b + c
# resultado

lado1 = float(input("Digite o valor do primeiro lado do  triângulo:"))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceirro lado do triângulo: "))

if lado1 and lado2 and lado3 > 0:
    perimetro = lado1 + lado2 + lado3
    print("O perímetro do triângulo é:", perimetro)

else:
    print("Digite um número válido!")
    