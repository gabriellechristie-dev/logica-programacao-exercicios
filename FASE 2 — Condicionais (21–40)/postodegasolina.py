"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

|Álcool | Até 25 litros, desconto de 2% por litro
Acima de 25 litros, desconto de 4% por litro

|Gasolina | Até 25 litros, desconto de 3% por litro
Acima de 25 litros, desconto de 5% por litro

Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,70 e o preço do litro
do álcool é R$ 1,90.
"""
litros = float(input("Digite a quantidade de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()    

if combustivel == 'A':
    preco_litro = 1.90
    if litros <= 25:
        desconto = 0.02 * preco_litro * litros
    else:
        desconto = 0.04 * preco_litro * litros
elif combustivel == 'G':
    preco_litro = 2.70
    if litros <= 25:
        desconto = 0.03 * preco_litro * litros
    else:
        desconto = 0.05 * preco_litro * litros
else:
    print("Tipo de combustível inválido.")
    exit()
valor_total = preco_litro * litros - desconto
print(f"Valor a ser pago: R$ {valor_total:.2f}")
