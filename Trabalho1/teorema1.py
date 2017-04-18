import sys
import math
import time
import random

def quociente(x,y,k):
	if k == 1:
		return 1
	return x**(k-1) + (y * quociente(x,y,k-1))

print ("\nTeorema 1: pow(x, n) - pow(y, n) eh divisivel por x - y para quaisquer x e y inteiros e todos valores de n inteiros e maiores do que zero.\n")

x = int(input(" x: "))
y = int(input(" y: "))
n = int(input(" n: "))

q = quociente(x, y, n)

print ("q[%d] = %d" % (n,q))

print ("\nCalculo de quantas execucoes acontecem por segundo. Para este calculo vamos usar valores aleatorios para x, y e k, entre 1 e 100.\n")

input()

random.seed()
t = 5
quantidadePorLoop = 0
inicio = time.time()
temp0 = 1

while(time.time() - inicio < t):
	quantidadePorLoop = quantidadePorLoop + 1
	q = quociente(x, y, n)
	#print ("q[%d] = %d" % (n,q))
	
	temp = time.time()
	if ((round(temp0)) != (round(temp))):
		temp0 = round(temp)
		temp2 = (round(temp)) - (round(inicio))
		print("Faltam %d segundos..." % (5 - temp2))

fim = time.time()
tempoExecucao = fim - inicio

print ("\nExecucoes: %d\nTempo: %.8f segundos\nExecucoes por segundo: %.4f\n" % (quantidadePorLoop, tempoExecucao, quantidadePorLoop/tempoExecucao))
