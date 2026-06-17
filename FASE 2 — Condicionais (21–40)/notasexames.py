"""
Em uma certificação são feitos são feitos 5 exames (I, II, III, IV e V). Escreva um
programa que leia as notas destes exames e imprima a classificação do aluno, sabendo
que a média é 70.
Classificação: 
A – passou em todos os exames;
B – passou em I, II e IV, mas não em III ou V;
C – passou em I e II, III ou IV, mas não em V.
Reprovado – outras situações
"""
nota1 = int(input("Digite a nota do exame 1: "))
nota2 = int(input("Digite a nota do exame 2: "))
nota3 = int(input("Digite a nota do exame 3: "))
nota4 = int(input("Digite a nota do exame 4: "))
nota5 = int(input("Digite a nota do exame 5: "))

if nota1 >= 70 and nota2 >= 70 and nota3 >= 70 and nota4 >= 70 and nota5 >= 70:
    print(f"Você foi aprovado nos 5 exames!\nExame 1: {nota1}pts\nExame 2: {nota2}pts\nExame 3: {nota3}pts\nExame 4: {nota4}pts\nExame 5: {nota5}pts.")
elif nota1 >= 70 and nota2 >= 70 and nota3 < 70 and nota4 >= 70 and nota5 < 70:
    print(f"Você foi aprovado apenas no exames 1,2 e 4!\nExame 1: {nota1}pts\nExame 2: {nota2}pts\nExame 3: {nota3}pts\nExame 4: {nota4}pts\nExame 5: {nota5}pts.")
elif nota1 >= 70 and nota2 >= 70 and nota3 >= 70 and nota4 >= 70 and nota5 < 70:
    print(f"Você foi aprovado apenas nos exames 1,2,3 e 4!\nExame 1: {nota1}pts\nExame 2: {nota2}pts\nExame 3: {nota3}pts\nExame 4: {nota4}pts\nExame 5: {nota5}pts.")
else:
    print("Reprovado!")