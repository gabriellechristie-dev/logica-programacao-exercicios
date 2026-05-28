"""
Um programa para gerenciar os saques de um caixa eletrônico deve possuir algum
mecanismo para decidir o número de notas de cada valor que deve ser disponibilizado
para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima"
no sentido de que as notas de menor valor fossem distribuídas em número mínimo
possível. Por exemplo, se a quantia solicitada fosse R$ 87,00, o programa deveria indicar
uma nota de R$ 50,00, três notas de R$ 10,00, uma nota de R$ 5,00 e duas notas de R$
1,00. Escreva um programa que receba o valor da quantia solicitada e retorne a
distribuição das notas de acordo com o critério da distribuição ótima (considere existir
notas de R$1,00; R$2,00; R$5,00; R$10,00; R$20,00; R$50,00 e R$100,00). 
"""

valor_saque = int(input("Digite o valor do saque: "))

notas_100 = valor_saque // 100
valor_saque = valor_saque % 100

notas_50 = valor_saque // 50
valor_saque = valor_saque % 50

notas_20 = valor_saque // 20
valor_saque = valor_saque % 20

notas_10 = valor_saque // 10
valor_saque = valor_saque % 10

notas_5 = valor_saque // 5
valor_saque = valor_saque % 5

notas_2 = valor_saque // 2
valor_saque = valor_saque % 2

notas_1 = valor_saque // 1

print(f"Notas de R$100,00: {notas_100}")
print(f"Notas de R$50,00: {notas_50}")  
print(f"Notas de R$20,00: {notas_20}")
print(f"Notas de R$10,00: {notas_10}")
print(f"Notas de R$5,00: {notas_5}")
print(f"Notas de R$2,00: {notas_2}")
print(f"Notas de R$1,00: {notas_1}")
    

