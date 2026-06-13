"""
Compra Online

Faça um programa para calcular o valor final de uma compra, a partir do valor da compra e do cupom de desconto. O cupom diz a porcentagemdo desconto.

"""
valor_da_compra = float(input("Digite o valor da compra: "))
cupom_desconto = float(input("Digite a porcentagem do cupom de desconto:"))

valor_desconto = valor_da_compra * (cupom_desconto / 100)
valor_final_compra = valor_da_compra - valor_desconto

print(f"O valor final da compra é R$ {valor_final_compra:.2f}.")