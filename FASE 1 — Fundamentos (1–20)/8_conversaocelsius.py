''' Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), ler um valor de temperatura em Fahrenheit e exibi-lo em Celsius'''

# pedir temperatura em fahrenheit 
# validar entrada
# calcular tempetatura em celsius
# mostrar temperatura em celsius

f = float(input("Digite a temperatura em Fahrenheit:"))

if f < -459.67:
    print("Digite um número válido")

else:

    c = 5/9 * ( f - 32)
    print(f"A temperatura em Celsius é: {c:.2f}°C")

