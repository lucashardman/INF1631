import sys
import math


def checa_divisao(x, y, n):
	a = pow(x,n)
	b = pow(y,n)
	c = a - b
	
	quociente = c/(x-y)

	return quociente

print "\nTeorema 1: pow(x, n) - pow(y, n) eh divisivel por x - y para quaisquer x e y inteiros e todos valores de n inteiros e maiores do que zero.\n"

print "Teorema do caso base: k = 1, x - y eh divisivel por x - y para quaisquer valores de x e y. Verdade pois o quociente sera sempre 1.\n"
x = int(input(" x: "))
y = int(input(" y: "))

quociente = checa_divisao(x, y, 1)
print "q[1] = ", quociente

print "\nTeorema do passo indutivo: assumindo que para um k fixo, pow(x, k) - pow(y, k) = q[k] * (x - y), onde q[k] eh um inteiro, podemos mostrar que pow(x, k+1) - pow(y, k+1) = q[k+1] * (x - y)"
x = int(input(" x: "))
y = int(input(" y: "))
n = int(input(" n: "))

quociente = checa_divisao(x, y, n)

print "q[",n,"] =",quociente

quociente = checa_divisao(x, y, n + 1)

print "q[",n,"+ 1] =", quociente

print "\n'Se vale para k, vale para k+1'. O teorema eh verdadeiro pois q[k+1] eh um inteiro assim como q[k], logo pow(x, k) - pow(y, k) eh divisivel por x - y para qualquer valor de k."