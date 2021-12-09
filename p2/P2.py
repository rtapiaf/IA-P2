# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:49:00 2018

@author: INF-322
"""

import random
import pandas as pd

#modelEnd = [[0,9,7,8],[9,0,10,15],[7,10,0,4],[8,15,4,0]]
#modelEnd = [0,1,2,3,4,5,6,7,8,9]
modelEnd = pd.read_csv("p22.csv",sep=";",header=None)
print (modelEnd)
largeIndividual = 5

num = 10 #Cantidad de individuos
generation = 1 #Generaciones
pressure = 3 #individual>2
#mutation_chance = 0.2

imin=0
imax=25

def individual(min, max):
    
    individuo=modelEnd
    random.shuffle(individuo)
    return individuo

def newPopulation():
    return [individual(imin,imax) for i in range(num)]

# Funcion la que se debe cambiar en funcion a f(x)
def functionType(individual):
    longitud=len(individual)
    suma=0
    for i in range(1,longitud):
        #print(recorrido[individual[i-1]][individual[i]])
        suma=suma+modelEnd[i-1][i]
    suma=suma+modelEnd[individual[i]][individual[0]]
    #print(suma)
    return suma,

def selection_and_reproduction(population):
    evaluating = [ (functionType(i), i) for i in population]
    print("eval",evaluating)
    evaluating = [i[1] for i in sorted(evaluating)]
    print("eval",evaluating)
    population = evaluating
    selected = evaluating[(len(evaluating)-pressure):]
    for i in range(len(population)-pressure):
        
        pointChange = random.randint(1,largeIndividual-1)
        father = random.sample(selected, 2)
        population[i][:pointChange] = father[0][:pointChange]
        population[i][pointChange:] = father[1][pointChange:]
        
        print("-------------")
        print(father[0])
        print(father[1])
        print(pointChange)
        print(population[i])
        
    return population

def mutation(individual):
    size = len(individual)
    for i in range(size):
        if random.random() < 2.0/largeIndividual:
            swap_indx = random.randint(0, size - 2)
            if swap_indx >= i:
                swap_indx += 1
            individual[i], individual[swap_indx] = \
                individual[swap_indx], individual[i]

    return individual,


# Principal
population = newPopulation()
print("\nPopulation Begin:\n%s"%(population))
population = selection_and_reproduction(population)
print("\Selection Population:\n%s"%(population))
population = mutation(population)
print("\Mutation Population:\n%s"%(population))
