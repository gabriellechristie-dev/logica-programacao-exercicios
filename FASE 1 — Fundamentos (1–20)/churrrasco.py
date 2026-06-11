"""
Faça um programa que avalie quanto cada pessoa deve contribuir para o churrasco de domingo. O programa deve receber a quantidade de pessoas e calcular o quanto de carne, linguiça e frango deve ser comprado e quanto cada pessoa deve pagar. Considere que cada pessoa consome 300g de carne (R$ 50,00/kg), 200g de linguiça (R$ 28,00/kg) e 150g de frango (R$ 22,00/kg).
"""
quantidade_pessoas = int(input("Digite a quantidade de pessoas para o churrasco:"))

carne_por_pessoa = 0.3  # kg
linguica_por_pessoa = 0.2  # kg
frango_por_pessoa = 0.15  # kg

preco_carne = 50.00  # R$ por kg
preco_linguica = 28.00  # R$ por kg
preco_frango = 22.00  # R$ por kg

total_carne = quantidade_pessoas * carne_por_pessoa
total_linguica = quantidade_pessoas * linguica_por_pessoa
total_frango = quantidade_pessoas * frango_por_pessoa

custo_carne = total_carne * preco_carne
custo_linguica = total_linguica * preco_linguica
custo_frango = total_frango * preco_frango

custo_total = custo_carne + custo_linguica + custo_frango

contribuicao_por_pessoa = custo_total / quantidade_pessoas

print(f"Total de carne necessária: {total_carne:.2f} kg")
print(f"Total de linguiça necessária: {total_linguica:.2f} kg")
print(f"Total de frango necessário: {total_frango:.2f} kg")
print(f"Custo total do churrasco: R$ {custo_total:.2f}")
print(f"Cada pessoa deve contribuir com: R$ {contribuicao_por_pessoa:.2f}")
