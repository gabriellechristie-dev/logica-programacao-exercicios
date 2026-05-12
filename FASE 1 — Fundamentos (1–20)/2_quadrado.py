''' Dado o tamanho do lado de um quadrado, calcular a área e o perímetro do mesmo. '''

# pedir tamanho do lado do quadrado
# validar entrada
# calcular area / L**2
# calcular perimetro / p = 4 * L

tam_lado = float(input("Digite o tamanho do lado em metros: "))

if tam_lado > 0:
    calculo_area = tam_lado ** 2
    print("Área: ", calculo_area)

    calculo_perimetro = 4 * tam_lado
    print("Perímetro: ", calculo_perimetro)
else:
    print("Digite um número válido! ")