""" 
Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma. 
"""

# pedir valor do raio
# validação do valor do raio 
# calcular área / área = pi * raio ** 2
# calcular perímetro / perímetro = 2 * pi * raio
# resultado


raio = float(input("Digite o valor do raio da circunferência:"))

if raio < 0:

    print("o valor do raio deve ser positivo")
else:
    pi = 3.14
    area = pi * raio ** 2
    perímetro = 2 * pi * raio

    print(f"A área da cinrcunferência é: {area:.2f}")
    print(f"O perímetro da circunferência é: {perímetro:.2f} ")

