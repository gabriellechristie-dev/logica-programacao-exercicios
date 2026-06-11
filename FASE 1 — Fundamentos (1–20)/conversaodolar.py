"""
Faça um programa para simular a conversão de um valor em real para dólar. Considere a cotação do dólar em R$ 5,42
"""
valor_real = float(input("Digite o valor em real:"))

dolar_cotacao = 5.42

valor_dolar = valor_real / dolar_cotacao
print(f"O valor {valor_real:.2f} em real equivale a U$ {valor_dolar:.2f} em dólar.")