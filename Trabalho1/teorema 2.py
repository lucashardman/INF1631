
# coding: utf-8

# In[8]:

import sys
import math
import time

def numbers (k ,m):
    newList = []
    
    #Caso Base
    if k == 1:
        for i in range (m):
            newList.append([i+1])
        return newList
    
    previousList = numbers(k-1,m)
    
    #para cara numero de k - 1 digitos
    for i in range (len(previousList)):
        #para cada dígito entre 0 e m-1
        for j in range (m):
            #se j+1 ainda nao foi utilizado no numero corrente, adicionar ao final deste e salvar na lista
            if(j+1) not in previousList[i]:
                newNumber = list(previousList[i])
                newNumber.append(j+1)
                newList.append(newNumber)
                
    return newList



print ("Teorema 2: O número de números inteiros cujos dígitos pertencem ao conjunto {1, 2, ..., m} de K dígitos diferentes é dado pelo produto m*(m-1)*...*(m-k+1)")

print ("\n Caso Base (k=1); Para formar um número inteiro de um dígito, basta escolher um número qualquer do conjunto. Sendo assim podemos formar m números.\n")

m = int(input(" m: "))
k = int(input(" k: "))

print ("\nPasso Indutivo: Seja um número qualquer com k-1 dígitos, com N possiilidades distintas de formação. Inserimos um novo dígito k ao final dele para termos um número com k dígitos. Dos m dígitos disponíveis, k-1 já foram usados.\n")
print ("Logo existem m-(k-1) = m-k-1 possibilidades para k e N*(m-k+1) possibilidades para nosso núero de k dígitos.")

resultado = numbers (m,k)
print (resultado)

