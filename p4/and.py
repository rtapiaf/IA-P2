# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 05:06:28 2021

@author: Ronald
"""

import numpy as np
	
def sigmoid(x, derivada=False):
   # return np.exp(x)/np.exp(x)+np.exp(x)
	    if derivada:
	        return x * (1 - x)
	    return 1 / (1 + np.exp(-x))
	
X = np.array([
	    [0,0,1],
	    [0,1,1],
	    [1,0,1],
	    [1,1,1],
	    ])
	
y = np.array([ [0], [0], [0], [1] ])
	
#np.random.seed(1)
	
n_capas = 3
n_conexiones = 4
n_salidas = 1
delta=0.001
	
syn0 = 2 * np.random.random((n_capas, n_conexiones)) - 1
syn1 = 2 * np.random.random((n_conexiones, n_salidas)) - 1
	
n_entrenamientos = 100000
n_error_entrenamiento = 10000
	
for j in range(n_entrenamientos):
    capa0 = X
    capa1 = sigmoid(np.dot(capa0, syn0))
    capa2 = sigmoid(np.dot(capa1, syn1))+delta
    	
    capa2_err = y - capa2
    	
    if (j % n_error_entrenamiento) == 0:
        print ("Error: " + str(np.mean(np.abs(capa2_err))))
    	
    	
    capa2_delta = capa2_err * sigmoid(capa2, derivada=True)
    	    
    capa1_err = capa2_delta.dot(syn1.T)
    	
    capa1_delta = capa1_err * sigmoid(capa1, derivada=True)
    	
    syn1 += capa1.T.dot(capa2_delta)
    syn0 += capa0.T.dot(capa1_delta)
	    
print ("Salida de entrenamiento")
print (capa2)
	
print(layer1)