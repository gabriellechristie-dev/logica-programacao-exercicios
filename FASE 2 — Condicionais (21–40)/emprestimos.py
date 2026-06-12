"""
Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do
empréstimo deve ser até dez vezes o valor da renda mensal do solicitante e o valor da
prestação deve ser no máximo 30% da renda mensal do solicitante. Escreva um programa
que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado e o
número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou
não ser concedido.
"""

renda_mensal = float(input("Digite o valor da sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo que deseja: "))
n_prestacoes = int(input("Digite o número de prestações que deseja pagar:"))

limite_emprestimo = renda_mensal  * 10
valor_prestacao = valor_emprestimo / n_prestacoes
limite_prestacao = renda_mensal * 0.3

if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido")
