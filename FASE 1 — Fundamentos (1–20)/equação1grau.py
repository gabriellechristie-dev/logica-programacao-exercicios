"""
Escreva um programa que calcule a raiz de uma equação do primeiro grau. A equação do primeiro grau tem a forma ax + b = 0, onde a e b são números reais e a é diferente de zero. O programa deve solicitar ao usuário os valores de a e b, calcular a raiz da equação e exibir o resultado. A raiz da equação pode ser calculada usando a fórmula x = -b / a.
"""

a = float(input("Digite o valor de a (diferente de zero): "))
b = float(input("Digite o valor de b : "))

if a == 0:
    print("O valor de a deve ser diferente de zero.")
else:
    raiz = -b / a
    print(f"A raiz da equação é: {raiz:.2f}")    
