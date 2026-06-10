"""
Escreva um algoritmo que leia 2 valores (x e y), que devem representar as coordenadas
de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o
ponto, ou se está sobre um dos eixos cartesianos ou na origem (x=y=0).0
"""
x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y:"))


if x == 0 and y == 0:
    print("O ponto está na origem")
elif x < 0 and y == 0:
    print("O ponto está no eixo X")
elif x > 0 and y == 0:
    print("O ponto está no eixo X")
elif x == 0 and y < 0:
    print("O ponto está no eixo Y")
elif x == 0 and y > 0:
    print("O ponto está no eixo Y")
elif x > 0 and y > 0:
    print("O ponto está no quadrante 1")
elif x < 0 and y > 0:
    print("O ponto está no quadrante 2")
elif x < 0 and y < 0:
    print("O ponto está no quadrante 3")
elif x > 0 and y < 0:
    print("O ponto está no qaudrante 4")
