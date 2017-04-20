import time
import sys

TIME_MAX = 5

#Função do algoritmo que estamos estudando
def geraTorneio(k, start = 1):
    if k == 1:
        return [[(start, start+1)]]
    t1 = geraTorneio(k-1, start)
    t2 = geraTorneio(k-1, 2**(k-1)+start)
    t = []
    for i in range(len(t1)):
        t.append(t1[i] + t2[i])
    times1 = range(start, 2**(k-1)+start)
    times2 = range(2**(k-1)+start, 2**(k)+start)
    for z in range(len(times1)):
        round = []
        for i in range(len(times1)):
            index1 = i
            index2 = (i + z) % len(times2)
            game = (times1[index1], times2[index2])
            round.append(game)
        t.append(round)
    return t

#Função para printar os resultados da divisão dos jogos
def printJogos(t):
    for round, games in enumerate(t):
        print("		Round #%02d" % (round+1))
        for game, teams in enumerate(games):
            print("		Game #%02d:		%d vs %d" % (game+1, teams[0], teams[1]))
	
print("	Digite um valor k > 1 fazer um teste: ")
k = int(input(" k: "))

t = 5
start = time.time()
execs = 0
inicio = time.time()
temp0 = 1

#Faz o teste varias vezes até completar 5 segundos
while(time.time() - inicio < t):

	execs += 1
	resultado = geraTorneio(k, 1) #Chama a função que estamos estudando
	temp = time.time()
	
	if ((round(temp0)) != (round(temp))): #Bloco apenas para printar a contagem de 5 segundos
		temp0 = round(temp)
		temp2 = (round(temp)) - (round(inicio))
		if ((6 - temp2) != 6):
			print(" Faltam %d segundos..." % (6 - temp2))

end = time.time()
tempoTotal = end - start

#Printa o resultado do teste do algoritmo
print ("\n Execucoes: %d" % execs)
print (" Tempo: %.3fs" % tempoTotal)
print (" Tempo por Execucao: %.6fms\n" % (1000*tempoTotal/execs))

#Printa o resultado da divisão dos jogos
pTeste = 1
pTeste = str(input(" Digite 0 caso queira ver o resultado: "))
if pTeste == "0":
	printJogos(resultado)