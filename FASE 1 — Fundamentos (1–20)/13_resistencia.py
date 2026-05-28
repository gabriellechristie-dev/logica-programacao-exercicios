""" 
Um circuito elétrico é composto de duas resistências R1 e R2 em paralelo, e ambas em sequência de uma resistência R3. Faça um algoritmo para calcular a resistência equivalente desse circuito.
"""

# pedir os valores de r1, r2 e r3
# validar entrada
# calcular resistência equivalente
# resultado

r1 = float(input("Digite o valor da resistência R1:"))
r2 = float(input("Digite o valor da resistência R2:"))
r3 = float(input("Digite o valor da resistência R3:"))

if r1 <= 0 or r2 <= 0 or r3 <= 0:
    print("Resistência inválida. Por favor, insira valores positivos.")

else:
    resistencia_equivalente = (r1 * r2) / (r1 + r2) + r3
    print(f"A resistência equivalente do circuito é: {resistencia_equivalente:.2f} ohms")

    