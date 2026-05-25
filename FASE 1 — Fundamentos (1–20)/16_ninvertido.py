''' 16. Escreva um programa para gerar o invertido de um número com três algarismos
(exemplo: o invertido de 498 é 894). '''


numero = int(input("Digite um número de três algarismos. Ex: 152: "))

unidade = (numero % 10) // 1
dezena = (numero % 100) // 10
centena = (numero % 1000) // 100

invertido = (unidade * 100) + (dezena * 10) + (centena * 1)
print(f"O número invertido é: {invertido}")
