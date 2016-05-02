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

print ("\n Caso Base (k=1);")

m = int(input( " m: "))

resultado = numbers (1,m)
print (resultado)

print ("\nPasso Indutivo;\nConsidere m>1 e k>1, tempo de execução máxima de cinco segundos")

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