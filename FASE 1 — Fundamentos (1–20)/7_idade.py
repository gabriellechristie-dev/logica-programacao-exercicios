''' Solicitar a idade de uma pessoa e informar na tela a idade em anos, meses e dias'''

# pedir idade
# validar entrada
# calcular idade em meses 
# calcular idade em dias
# mostrar idade em anos, meses e dias

idade = int(input("Digite a sua idade: "))
 
if idade <= 0:
    print("Digite um número inteiro válido")

else:
    idade_meses = idade * 12
    idade_dias = idade * 365

    print(f"Sua idade é {idade} anos, {idade_meses} meses e {idade_dias} dias")


            