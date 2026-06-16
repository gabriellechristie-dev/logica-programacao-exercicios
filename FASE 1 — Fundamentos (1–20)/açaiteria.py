"""
Açaiteria

Faça um programa para calcular o total de uma venda de açaí a partir das quantidades compradas para cada tamanho: pequeno, médio e grande, sabendo que o valor do açaí é R$ 13,50, R$ 15,00 e R$ 17,50 respectivamente. O programa também deve receber o valor do cupom de desconto em porcentagem.
"""
açai_p = int(input("Digite a quantidade de açaí P desejado:"))
açai_m = int(input("Digite a quantidade de açaí M desejado:"))
açai_g = int(input("Digite a quantidade de açaí G desejado:"))

cupom = int(input("Digite o valor do cupom adquirido:"))

valor_p = 13.50
valor_m = 15.00
valor_g = 17.50


total = ((açai_p * valor_p) + (açai_m * valor_m) + (açai_g * valor_g)) * 0.5

print(f"Quantidade de açaí P:{açai_p}\nQuantidade de açaí M:{açai_m}\nQuantidade de açaí G:{açai_g}\nValor do cupom de desconto:{cupom}\nValor total da compra:{total}")