"""
Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano (x1, y1) e (x2, y2), escreva a distância entre eles. A fórmula para calcular a distância entre dois pontos é dada por: d = √((x2 - x1)² + (y2 - y1)²)
"""

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  
print(f"A distância entre os pontos é: {distancia:.2f}")
