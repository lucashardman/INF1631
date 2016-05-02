def numbers (k ,m):
    newList = []

    # Caso base
    if k == 1:
        for i in range(m):
            newList.append([i+1])
        return newList

    previousList = numbers(k-1,m)

    # para cada numero de k - 1 digitos
    for indexK in range(len(previousList)):
        # para cada digito entre 0 e m-1
        for indexM in range(m):
            # se indexM+1 ainda nao foi utilizado no numero corrente, adicionar ele como um digito novo
            if (indexM+1) not in previousList:
                newNumber = list(previousList[indexK])
                newNumber.append(indexM+1)
                newList.append(newNumber)

    return newList

if __name__ == '__main__':
    
    from time import time
    import sys

TIME_MAX = 5
EXEC_MAX = 5

print ("Teorema 2: O número de números inteiros cujos dígitos pertencem ao conjunto {1, 2, ..., m} de K dígitos diferentes é dado pelo produto m*(m-1)*...*(m-k+1)")

print ("\n Caso Base (k=1); Para formar um número inteiro de um dígito, basta escolher um número qualquer do conjunto. Sendo assim podemos formar m números.\n")

m = int(input( " m: "))

resultado = numbers (1,m)
print (resultado)

print ("\nPasso Indutivo: Seja um número qualquer com k-1 dígitos, com N possiilidades distintas de formação. Inserimos um novo dígito k ao final dele para termos um número com k dígitos. Dos m dígitos disponíveis, k-1 já foram usados.\n")
print ("Logo existem m-(k-1) = m-k-1 possibilidades para k e N*(m-k+1) possibilidades para nosso núero de k dígitos.")
print ("Considere m>1 e k>1, tempo de execução mínimo de cinco segundos")

m = int(input(" m: "))
k = int(input(" k: "))

start = time()
execs = 0

while not (time()-start>TIME_MAX):
    execs+=1
    resultado=numbers(k,m)
end = time()
elapsed = end-start

print (resultado)

print ("Total: %d" %len(resultado))
print ("Execuções: %d" % execs)
print ("Tempo: %.3fs" % elapsed)
print ("Tempo por Execução: %.6fms" % (1000*elapsed/execs))