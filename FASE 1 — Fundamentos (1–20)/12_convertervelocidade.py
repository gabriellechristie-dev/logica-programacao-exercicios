""" 
Faça um algoritmo que transforme uma velocidade fornecida em m/s pelo usuário para Km/h. Para tal, multiplique o valor em m/s por 3,6.
"""

# pedir velocidade em m/s
# validar entrada 
# converter para km/h -- > multiplicar por 3,6
# resultado

velocidade = float(input("Digite a velocidade em m/s:"))

if velocidade < 0:
    print("Velocidade inválida. Por favor, insira um valor positivo.")

else:
    velocidade_km = velocidade * 3.6
    print(f"A velocidade em km/h é: {velocidade_km:.2f}")





