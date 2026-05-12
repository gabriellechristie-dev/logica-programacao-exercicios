''' Converter um inteiro informado menor que 32 para sua representação em binário'''

# pedir numero inteiro menor que 32
# validar entrada
# converter numero para binario -- dividir o numero por 2 e guardar o resto, repetir o processo com o resultado da divisão até chegar a 0, os restos formam o número binário
# mostrar resultado

n = int(input("Digite um número inteiro menor que 32:"))

if n < 0  or n >= 32:
    print("Digite um número válido")

else:
    binario = ""
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2
    print(f"O número em binário é: {binario}")
