import sys
import math
import time
import random

def quociente(x,y,k):
	if k == 1:
		return 1
	return x^(k-1) + (y * quociente(x,y,k-1))

print "\nTeorema 1: pow(x, n) - pow(y, n) eh divisivel por x - y para quaisquer x e y inteiros e todos valores de n inteiros e maiores do que zero.\n"

print "Teorema do caso base: k = 1, x - y eh divisivel por x - y para quaisquer valores de x e y. Verdade pois o quociente sera sempre 1.\n"
x = int(input(" x: "))
y = int(input(" y: "))

q = (pow(x, 1) - pow(y, 1))/(x - y)
print "q[1] = ", q

print "\nTeorema do passo indutivo: assumindo que para um k fixo, pow(x, k) - pow(y, k) = q[k] * (x - y), onde q[k] eh um inteiro, podemos mostrar que pow(x, k+1) - pow(y, k+1) = q[k+1] * (x - y)"
x = int(input(" x: "))
y = int(input(" y: "))
n = int(input(" n: "))

q = quociente(x, y, n)

print "q[%d] = %d" % (n,q)

print "\nCalculo de quantas execucoes acontecem por segundo. Para este calculo vamos usar valores aleatorios para x, y e k, entre 1 e 100.\n"

input()

random.seed()
t = 5
quantidadePorLoop = 0
inicio = time.time()
while(time.time() - inicio < t):
	x = random.randint(1,100)
	y = random.randint(1,100)
	n = random.randint(1,100)

	quantidadePorLoop = quantidadePorLoop + 1
	q = quociente(x, y, n)
	print "q[%d] = %d" % (n,q)

fim = time.time()
tempoExecucao = fim - inicio

print "\nExecucoes: %d\nTempo: %.8f segundos\nExecucoes por segundo: %.4f\n" % (quantidadePorLoop, tempoExecucao, quantidadePorLoop/tempoExecucao)
