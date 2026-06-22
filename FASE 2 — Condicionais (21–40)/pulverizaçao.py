"""
Uma Cia de pulverização utiliza avião para pulverizar lavouras. Os custos de
pulverização dependem do tipo de praga e da área a ser contratada conforme a tabela:

Tipo 1 – ervas daninhas R$ 50,00 por acre;
Tipo 2 – gafanhotos R$ 100,00 por acre;
Tipo 3 – broca R$ 150,00 por acre;
Tipo 4 – todos acima R$ 250,00 por acre.

Se a área a ser pulverizada for superior a 1000 acres, o fazendeiro tem um desconto de
5%. Em adição, qualquer fazendeiro cujo custo for maior do que R$ 750,00 tem um
desconto de 10% sobre o valor que ultrapassar os R$ 750,00. Caso ambos os descontos se
aplicam o da área é calculado antes. 

Fazer um algoritmo que leia: o tipo de pulverização
(1 a 4) e área a ser pulverizada; e imprima o valor a ser pago.
"""
tipo = int(input("Digite o número do tipo do pulverização: "))
area = float(input("Digite em metros a área a ser pulverizada: "))


if tipo == 1:
    custo_total = 50 * area
elif tipo == 2:
    custo_total = 100 * area
elif tipo == 3:
    custo_total = 150 * area
elif tipo == 4:
    custo_total = 250 * area
else:
    print("Digite um tipo de 1 a 4!")
    exit()
    
if area > 1000:
    desconto = custo_total * (5/100) 
    custo_final = custo_total - desconto
else:
    custo_final = custo_total

if custo_final > 750:
    excedente = custo_final - 750 
    desconto = excedente * 0.10
    custo_final -= desconto

print(f"O valor final a ser pago será:{custo_final:.2f}")