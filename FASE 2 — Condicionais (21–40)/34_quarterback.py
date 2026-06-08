"""
No Futebol Americano, usa-se o Quarterback Rating como um índice que indica o
desempenho do quarterback (quando maior, melhor). Ele é calculado como indicado a
seguir: 

1 - Calcula-se o percentual de passes completados em relação aos passes tentados
pelo quarterback. Deste valor subtrai-se 0,3 e divide-se por 0,2. Este valor não deve ser
maior que 2,375 ou menor que 0 (caso seja, ajusta-se o valor para 2,375 ou 0,
respectivamente).

2 -Em seguida, calcula-se a razão de jardas passadas pela quantidade de passes tentados.
Deste valor, subtrai-se 3 e divide-se por 4. Novamente, este valor não deve ser maior que
2,375 ou menor que 0 (caso seja, procede-se como no caso anterior).

3 -Agora, calcula-se a razão de passes para touchdows pelo número de passes tentados.
Divide-se o valor por 0,05. Mais uma vez, este valor não deve ser maior que 2,375 ou
menor que 0 (caso seja, procede-se como de costume).

4 - Então, calcula-se a razão entre passes interceptados e o número de passes tentados. Deste
valor, subtrai-se 0,095 e divide-se o resultado por 0,04. Como de praxe, este valor não
deve ser maior que 2,375 ou menor que 0 (caso seja, atua-se como explicado).

5 - O quarterback rating é calculando somando-se as quatro parcelas anteriores,
multiplicando a soma por 100 e dividindo-se o produto por 6.

Escreva um programa, que leia o número de passes tentados, o número de passes
completos, o número de jardas passadas, o número de passes para touchdown e o número
de passes interceptados e informe o QB Rating do quarterback.
"""

passes_tentados = int(input("Digite o número de passes tentados: "))
passes_completos = int(input("Digite o número de passes completos: "))
jardas_passadas = int(input("Digite o número de jardas passadas: "))
passes_touchdown = int(input("Digite o número de passes para touchdown: "))
passes_interceptados = int(input("Digite o número de passes interceptados: "))

percentual_completos = (passes_completos / passes_tentados - 0.3) / 0.2
razao_jardas = (jardas_passadas / passes_tentados - 3) / 4
razao_touchdown = (passes_touchdown / passes_tentados) / 0.05
razao_interceptados = (passes_interceptados / passes_tentados - 0.095) / 0.04

# Ajustando os valores para não serem maiores que 2,375 ou menores que 0
percentual_completos = max(0, min(percentual_completos, 2.375))
razao_jardas = max(0, min(razao_jardas, 2.375))
razao_touchdown = max(0, min(razao_touchdown, 2.375))
razao_interceptados = max(0, min(razao_interceptados, 2.375))
qb_rating = (percentual_completos + razao_jardas + razao_touchdown + razao_interceptados) * 100 / 6
print(f"QB Rating: {qb_rating:.2f}")



