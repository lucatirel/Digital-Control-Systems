# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:51:08 2021

@author: luca9
"""
# IMPORTS AND PARAMETERS
# Importing libraries
import numpy as np

# Polynomial definition
P = [1.00000, 0.90000, -1.12000, -2.50400, -1.57240, -0.37740]

def Jury(P):
    # ASSUMPTIONS CHECK
    # 1) Real coefficients
    for p in P:
        if type(p) == complex:
            print("The coefficient " + str(p) + " is complex. The first assumption is violated.\n")
            return None
        
    # 2) Pn not zero
    if P[0] == 0:
        print("The higher order coefficient is zero. Second assumption has been violated since polynomial has not degree n.\n")
        P = P[1:]
        print("New polynomial of degree n-1 has been created eliminating Pn coefficient.\n")
    
    # 3) P0 not zero
    if P[len(P)-1] == 0:
        print("The lower order coefficient is zero. Third assumption has been violated since polynomial has a root in zero.\n")
        P = P[:len(P)-2]
        print("New polynomial has been created factorizing the root in zero.\n")
        
    # 4) Polynomial has no root on the unit circle
    Z = np.roots(P)
    for z in Z:
        if z.real**2 + z.imag**2 == 1:
            print("The root " + str(z) + " lies on the Unit Circle. Fourth assumption has been violated.")
            return None # or DO PERTURBATION HERE
               
        
    # RAIBLE'S TABLE CREATION
    n = len(P)-1
    
    TAB = [P]
    
    for r in range(1,n+1):
        row = []
        c1 = 0
        c2 = len(TAB[r-1]) - 1
        k = TAB[r-1][len(TAB[r-1])-1]/TAB[r-1][0]
        k = round(k,5)
        
        for j in range(len(TAB[r-1])-1):
            x = (TAB[r-1][c1])-k*(TAB[r-1][c2])
            
            c1 += 1
            c2 -= 1
            
            x = round(x, 5)
            row.append(x)
            
        TAB.append(row)
    
    # JURY TEST ON RAIBLE'S TABLE
    INSIDE , OUTSIDE = [] , []

    # Case A) Pn > 0
    if P[0] > 0:        
        for lista in TAB[1:]:
            if lista[0] > 0:
                INSIDE.append(lista[0])
            elif lista[0] < 0:
                OUTSIDE.append(lista[0])
                
    # Case B) Pn < 0
    elif P[0] < 0:        
        for lista in TAB[1:]:
            if lista[0] < 0:
                INSIDE.append(lista[0])
            elif lista[0] > 0:
                OUTSIDE.append(lista[0])
                
    # Check number of roots:
    print("Order of Polynomial: ")
    print(n)
    print("Number of Inside + Outside roots: ")
    print(len(INSIDE) + len(OUTSIDE))
    print("\nINSIDE-ROOT coefficients:")
    print(INSIDE)
    print("OUTSIDE-ROOT coefficients:")
    print(OUTSIDE)
    print("\n\nRaible's Table:\n")

    return TAB, INSIDE, OUTSIDE, P



# CODE EXECUTION
TAB, INSIDE, OUTSIDE, P = Jury(P)
try:
    for row in TAB:
        print(row)
    print("\n")
    
    if len(OUTSIDE) > 0:
        print("The following coefficients:\n")
        print(P)
        print("\ngenerates a polynomial that is NOT STABLE, since it has " + str(len(OUTSIDE)) + " roots outside the Unit Circle.")
    else:
        print("The given polynomial is STABLE.") 
except:
    pass       
