
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 21:25:32 2018

Project description: Finding the lowest energy for a wave function using quantum Monte Carlo simulation for a one dimensional harmonic oscillator.

@author: Vidya Venkatesan
"""
'''Libraries'''

import numpy as np                            
import matplotlib.pyplot as plt            
import random as rn  
import math as m 

''' Global variables'''
x = 6.0
dx = 0.1 
num_sim = 1

''' Takes in number (x) and creates a list from -x to x.    
    Args: 
        x [list of float values] the range of values for position
    Returns: 
        r: [list of float values] contains numbers from -x to x 
    Side Effects :
        no side effects 
      '''

def position(x, dx):
    r = [ ]
    t = int(((x*2)/dx)+1)
    for i in range(t):
        r.append(-x+dx*i)
    return r


''' Takes the position r and outputs the wave function at respective positions.
    Args: 
        r [list of float values] the position of wavefunction
    Returns: 
        phi(r) [list of float values] the wave function
    Side Effects : 
        No side effects
        '''
def wavefunction(r): 
    phi = [m.cos(i) for i in r]
    #phi = [i*i for i in r]
    #phi = [1/(m.pi** (1/4)) * m.exp(- (i**2)/2) for i in r]
    return phi

''' Takes the list phi and adds 0 element in the beginning and at the end.
    Args: 
        phi: [list of values] wavefunction
    Returns:
        phi: [list of values] with a 0 in the beginning and at the end
    Side Effects: 
        No side effects 
        '''
def addzeroes(phi):
    a = 0
    phi = [a] + phi +[a]  
    return phi

''' Takes the list phi and deletes 0 in the beginning and at the end.
    Args: 
        phi: [list of float values] wavefunction
    Returns:
        phi: [list of float values] wavefunction without a 0 at the beginning and at the end
    Side Effects:
        No side effects
        '''
def deletezeroes(phi):
    del phi[0]
    del phi[-1]
    return phi

'''  Takes in the position and wave function and gives out the Kinetic energy value 
    Args:
        phi: [list of float values] the wavefunction
        r: [list of float values] the position of wavefunction
    Returns:
         k : [list of float values] it is the kinetic energy value 
    Side Effects : No side effects
'''
def kinetic(phi,r,dx): 
     k = []
     phi = addzeroes(phi)   # adds 0 in the beg and end
     m = len(phi)-2         #original length 23 makes it 21
     for i in range(m):                           # It takes elements from 0 to 20 and calculates K value
       k.append(( 2 * phi[i+1] - phi[i+2] - phi[i])/( 2 * (dx**2)))
     phi = deletezeroes(phi)    
     return k

''' Takes in kinetic energy, position and wavefunction and spills out the energy 
    Args:
        r : (list of values) it is the position of the wave function
        phi: (list of float val) my wave function
    Returns:
        E0: [list of float values] Initial Energy of the harmonic oscillator
    Side Effects :
        t : (int) just a variable to store x+1 
        index2 : (int) print this index and its log
        f1: [list of float values] to store the numerator part of integration
        f2, f3: [list of float values] to store the denominator part of integration
        '''
def Energyinitial(k, phi, r, dx):                                  

    r = np.array(r)
    U = 0.5 *( r**2) 
    v = U * phi
    Hop = k  + v                                            
    phi = np.array(phi)
    Hop = np.array(Hop) 
    f1 = []
    f1 = phi * Hop * dx
    f2 = []
    f2 = [i*i for i in phi] 
    f2 = np.array(f2)
    f3 = f2 * dx
    H1 = np.trapz(f1)                                   
    H2 = np.trapz(f3)                            
    E0 = float(H1)/float(H2)  
    return E0

""" Takes in the position, wavefunction, kinetic energy, Initial Energy 
    and performs monte carlo simulation to find the lowest posible Energy 
    value for the harmonic oscillator
    Args:
        r: [list of values] 
        Kr: [list of float values] Kinetic energy of randomly selected value
        Er: [list of float values] Energy of randomly selected position
        dxr: [float] random change from -delta to +delta
        
    Returns:
        E: [list of float values] the lowest possible enrgy value for the given wavefunction
        
    Side Effects : 
        num_sim: [int] the steps where things are being calculated
        Enow: [list of float values] Value of Energy at that step
        phinow: [list of float values] Value of the wave function at that step
        n: [int] length of position list
        Graphs position vs wavefunction before randomization
        Graphs position vs wavefunction after randomization
        Graphs steps vs Energy after randomization
        
        """

def Monte_carlo(phi, k,E0,r, dx):  #insert numsim
     num_sim = 1500000
     steps = []
     E_plot = []
     for i  in range(num_sim):
         steps.append(i)
         n= len(r)  
         
         if i ==0:
             E_now = E0
             E = E0
             phi_now = phi
             
             # Plots position vs Wavefunction before applying monte carlo technique
             plt.figure()  
             plt.plot(r, phi_now, '-b') 
             plt.title("Position(r)  vs Wavefunction(phi)  without Randomization")
             plt.xlabel("Position(r)")
             plt.ylabel("Wavefunction(phi)")
             plt.show()
         
         index_rand = rn.randint(0,n-1)
         dxr =round(rn.uniform(-0.09, 0.09),2)
         phir = phi_now[:]
             
         phir[index_rand] = phir[index_rand]+ dxr
         Kr = kinetic(phir,r,dx)
         
        
         Er = Energyinitial(Kr, phir, r, dx)
         E_plot.append(E_now)
         
        
         if(Er < E_now):
             E_now = Er 
             E = E_now
             
             phi_now = phir[:]
        
         if i == num_sim:
             E = E_now
     
     # Plots number of steps (i) vs Energy at i
     plt.figure()  
     plt.plot(steps, E_plot, '-r') 
     plt.title("Steps(i)  vs E(i) after Randomization")
     plt.xlabel("Steps(r)")
     plt.ylabel("Energy(E(i))")
     plt.show()
     
     # Plots position vs Wavefunction after applying monte carlo technique
     plt.figure()  
     plt.plot(r, phi_now, '-b') 
     plt.title("Position(r)  vs Wavefunction(phi)  after Randomization")
     plt.xlabel("Position(r)")
     plt.ylabel("Wavefunction(phi)")
     plt.show()
     print('E_initial= ', E0)
     print('E_final= ', E)
     return E

''' The main function allows the implementation of unit testing '''


def main():
    
    r = position(x,dx)
    phi =  wavefunction(r)
    k = kinetic(phi,r,dx)  
    E0 = Energyinitial(k, phi, r, dx)    
    E = Monte_carlo(phi, k,E0,r, dx)
    

if __name__ == '__main__': main()
   

''' End of the code'''
    
  
    


