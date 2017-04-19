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
    
def printJogos(t):
    for round, games in enumerate(t):
        print("		Round #%02d" % (round+1))
        for game, teams in enumerate(games):
            print("		Game #%02d:		%d vs %d" % (game+1, teams[0], teams[1]))

if __name__ == '__main__':
    from time import time
    import sys

    TIME_MAX = 5

	
	
    print("	Digite um valor k > 1 fazer um teste: ")
    k = int(input(" k: "))

    start = time()
    execs = 0
	
    while not (time() - start > TIME_MAX):
        execs += 1
        resultado = geraTorneio(k, 1)
    end = time()
    tempoTotal = end - start

    #printJogos(resultado)
    print (" Execucoes: %d" % execs)
    print (" Tempo: %.3fs" % tempoTotal)
    print (" Tempo por Execucao: %.6fms" % (1000*tempoTotal/execs))
	#pTeste = 1
	#print("	Digite 0 caso queira ver o resultado: ")
    #pTeste = int(input("	Digite 0 caso queira ver o resultado: "))
	#if pTeste == 0:
	#	printJogos(resultado)