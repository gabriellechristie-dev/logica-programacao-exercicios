''' Ler um número inteiro e exibir o seu sucessor. '''

# pedir valor 
# validar entrada
# calcular sucessor / sucessor = numero +  1
# resultado

numero = int(input("Digite um número inteiro:"))

if numero > 0:
    sucessor = numero + 1
    print("O sucessor do número digitado é:", sucessor)
else:
    print("Digite um número inteiro válido!")
    