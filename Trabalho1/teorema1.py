import sys
import math


def checa_divisao(x, y, n):
	a = pow(x,n)
	b = pow(y,n)
	c = a - b
	
	quociente = c/(x-y)

	print(quociente)

print "\nTeorema 1: pow(x, n) - pow(y, n) eh divisivel por x - y para quaisquer x e y inteiros e todos valores de n inteiros e maiores do que zero.\n"

print "Teorema do caso base: k = 1, x - y eh divisivel por x - y para quaisquer valores de x e y. Verdade pois o quociente sera sempre 1.\n"
x = int(input(" x: "))
y = int(input(" y: "))

checa_divisao(x, y, 1)

print "Teorema do passo indutivo: assumindo que para um k fixo, pow(x, k) - pow(y, k) = q[k] * (x - y), onde q[k] eh um inteiro, podemos mostrar que pow(x, k+1) - pow(y, k+1) = q[k+1] * (x - y)"
x = int(input(" x: "))
y = int(input(" y: "))
n = int(input(" n: "))
