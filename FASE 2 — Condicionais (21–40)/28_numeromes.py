"""
Escreva um programa que leia o número equivalente ao mês e imprima a quantidade de
dias deste mês.
"""

mes  = int(input("Digite o número do mês:"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("O mês tem 31 dias.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("O mês tem 30 dias.")
elif mes == 2:
    print("O mês tem 28 ou 29 dias.")
else:
    print("Número do mês inválido.")
