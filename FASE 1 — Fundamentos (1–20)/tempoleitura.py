"""
Você lê rápido?

Faça um programa que calcule o tempo que um livro será lido por uma pessoa a partir do nome do livro, do total de páginas e do tempo em segundos de leitura por págin
"""
nome = input("Digite seu nome: ")
nome_livro = input("Digite o nome do livro que irá ler: ")
paginas = int(input("Digite o número de páginas do livro: "))
tempo_leitura = int(input("Digite em quantos segundos você lê uma página: "))

segundos_totais_leitura = paginas * tempo_leitura
conversao_horas = segundos_totais_leitura / 3600

print(f"{nome} você finalizará a leitura do livro {nome_livro} em aproximadamente {conversao_horas:.2f} horas. ")