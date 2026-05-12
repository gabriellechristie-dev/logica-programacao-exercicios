''' Ler dois números inteiros e exibir o quociente e o resto da divisão inteira entre eles. '''

# pedir primeiro valor 
# pedir segundo valor
# validar entrada 
# calcular quociente - quociente = n1 // n2
# calcular resto - resto = n1 % n2
# resultado 

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 > 0 and n2 > 0:
    quociente = n1 // n2
    resto = n1 % n2

    print("O quociente da divisão inteira entre os números digitados é: ", quociente)

    print("O resto da divisão inteira entre os números digitados é:", resto)

else:
    print("Digite números inteiros válidos!")