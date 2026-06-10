"""
Faça um algoritmo para calcular a nota semestral de um aluno. A nota semestral é obtida pela média aritmética entre a nota de 2 bimestres. Cada nota de bimestre é composta por 2 notas de provas.
"""

# pedir nota do primeiro bimestre
# pedir nota do segundo bimestre
# validar entrada
# calcular nota semestral
# mostrar resultado


nota_1bimestre = float(input("Digite a nota do primeiro bimestre:"))
nota_2bimestre = float(input("Digite a nota do segundo bimestre:"))

if nota_1bimestre < 0 or nota_1bimestre > 10 or nota_2bimestre < 0 or nota_2bimestre > 10:
    print("Digite um número válido")
else:
    nota_semestral = (nota_1bimestre + nota_2bimestre) / 2
    print(f"A nota semestral do aluno é: {nota_semestral:.2f}") 

