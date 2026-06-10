"""
Escreva um programa que leia um caracter e diga se ele é uma vogal, consoante, número
ou um símbolo (qualquer outro caracter, que não uma letra ou número).
"""
caracter = input("Digite um caracter: ")

if caracter.isalpha():
    if caracter.lower() in 'aeiou':
        print("O caracter é uma vogal.")
    else:
        print("O caracter é uma consoante.")
elif caracter.isdigit():
    print("O caracter é um número.")
else:
    print("O caracter é um símbolo.")


