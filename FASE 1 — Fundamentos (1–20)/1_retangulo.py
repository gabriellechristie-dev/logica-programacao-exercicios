''' Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro '''

    # pedir tamanho da base
    # pedir altura
    # validar entrada
    # calcular area / area = b * h
    # calcular perimetro / p = 2 * (b+h)


base = float(input("Digite o tamanho da base em metros: " ))
altura =  float(input("Digite a altura em metros: "))

if base and altura > 0:
    calculo_area = base * altura 
    print ("Área: ", calculo_area)

    calculo_perimetro =  2 * ( base + altura)
    print ("Perimetro:", calculo_perimetro)
else:
    print("Digite um número válido!")
    

