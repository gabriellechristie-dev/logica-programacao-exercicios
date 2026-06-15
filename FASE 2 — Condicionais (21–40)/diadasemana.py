"""
Escreva um programa que leia um número inteiro de 1 a 7 e informe o dia da semana
correspondente, sendo domingo o dia de número 1. Se o número não corresponder a um
dia da semana, mostre uma mensagem de erro.
"""
dias_da_semana = ["domingo","segunda","terça","quarta","quinta","sexta","sábado"]

dia = int(input("Digite um número inteiro: "))

if dias_da_semana[dia - 1]:
    print(f"Hoje é {dias_da_semana[dia-1]}!")
else:
    print("Número inválido!")