#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:17:39 2026

@author: basti07
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random
from scipy import ndimage

GRIDSIZE = 100
f = 0.06
k = 0.06
Du = 0.2097
Dv = 0.1050



# Laplace Berechnung für einzelnes Feld
def neighbours(A, i, j):
    i_nxt = (i+1)%GRIDSIZE
    i_prev = (i-1)%GRIDSIZE
    j_nxt = (j+1)%GRIDSIZE
    j_prev = (j-1)%GRIDSIZE
    
    return A[i_nxt][j] + A[i_prev][j] + A[i][j_nxt] + A[i][j_prev] - 4*A[i][j]

# Laplace Berechnung mit np.roll()
def laplaceRoll(Z):
    return (np.roll(Z, 1, 0) + np.roll(Z, -1, 0) +
            np.roll(Z, 1, 1) + np.roll(Z, -1, 1) - 4 * Z)

# Iterative Laplace Berechnung
def laplaceIterative(U, V):
    laplaceU = np.zeros((GRIDSIZE,GRIDSIZE))
    laplaceV = np.zeros((GRIDSIZE,GRIDSIZE))
    
    for i in range(GRIDSIZE):
        for j in range(GRIDSIZE):
            laplaceU[i, j] = neighbours(U, i, j)
            laplaceV[i, j] = neighbours(V, i, j)
            
        return laplaceU, laplaceV



 
'''
# step() mit Iteration über alle Felder:
def step(U, V, f, k, Du, Dv):
    Ut = np.zeros(U.shape)
    Vt = np.zeros(V.shape)
    
    for i in range(GRIDSIZE):
        for j in range(GRIDSIZE):
            uvv = U[i][j] * V[i][j] * V[i][j] 
            
            Ut[i][j] = U[i][j] - uvv + f*(1-U[i][j]) + Du*neighbours(U, i, j)
            Vt[i][j] = V[i][j] + uvv - (f+k)*V[i][j] + Dv*neighbours(V, i, j)

    return Ut, Vt
'''


# step() mit numpy Array Operationen:
def step(U, V, f, k, Du, Dv):
    uvv = U*V*V
    
    # Laplace mit eigener Funktion
    '''
    laplace()
    U += -uvv + f*(1-U) + Du*laplace(U)
    V += uvv - (f+k)*V + Dv*laplace(V)
    '''
    
    # Laplace mit ndimage Approximation
    U += -uvv + f*(1-U) + Du*ndimage.laplace(U)
    V += uvv - (f+k)*V + Dv*ndimage.laplace(V)
    
    return U, V

   

# Startstörung:
 
# Quadrat in Mitte:
def squareStart(U, V):
    U[45:50, 45:50] = 0.5
    V[45:50, 45:50] = 0.25
    return U, V

# n zufällige Störungen
def randomStart(n, U, V):
    for i in range(n):
        x = random.randint(0,100)
        y = random.randint(0,100)
        U[x:x+5, y:y+5] = 0.5
        V[x:x+5, y:y+5] = 0.25
    return U, V



# Simulation mit n Schritten
def simulate(n, U, V, f, k, Du, Dv):
    plt.imshow(V, cmap="inferno")
    plt.show()
    start = time.time()
    
    for i in range(n):
        if i%(n/20)==0: print("Step: ", i, "/", n)
        
        U, V = step(U, V, f, k, Du, Dv)
        
    print("Simulation time: ", time.time()-start)
    plt.imshow(V, cmap="inferno")
    plt.show()


U = np.ones((GRIDSIZE, GRIDSIZE))
V = np.zeros((GRIDSIZE, GRIDSIZE))

# U, V = squareStart(U, V)
U, V = randomStart(3, U, V)

simulate(5000, U, V, f, k, Du, Dv)


    