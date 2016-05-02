def tournament(k, start = 1):
    # Caso base
    if k == 1:
        return [[(start, start+1)]]
    t1 = tournament(k-1, start)
    t2 = tournament(k-1, 2**(k-1)+start)
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
    
def print_tournament(t):
    for round, games in enumerate(t):
        print("		Round #%02d" % (round+1))
        for game, teams in enumerate(games):
            print("		Game #%02d:		%d vs %d" % (game+1, teams[0], teams[1]))

if __name__ == '__main__':
    from time import time
    import sys

    TIME_MAX = 5
    EXEC_MAX = 5

    print("	Caso Base (k=1)")
    resultado=tournament(1)
    print_tournament(resultado)

    print("	Passo Indutivo (k>1)")
    k = int(input(" k: "))

    start = time()
    execs = 0
    while not (execs > EXEC_MAX and time() - start < TIME_MAX):
        execs += 1
        resultado = tournament(k)
    end = time()
    tempoTotal = end - start

    print_tournament(resultado)
    print (" Execuções: %d" % execs)
    print (" Tempo: %.3fs" % tempoTotal)
    print (" Tempo por Execução: %.6fms" % (1000*tempoTotal/execs))
