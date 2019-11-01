# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import os 
import scipy.special as sp
import scipy.optimize as op
import matplotlib.pyplot as mpl




def search_files(path):    
    for subdirs,dirs,fname in os.walk(path):
       for files in fname:
           data = np.genfromtxt(files,skip_header=2)
           x= data[0,2]
           t= data[:,0]/86400
           c= data[:,1]
           arrpos = np.argmax(c>0.5)
           v=x/t[arrpos]
           
def ob(beta,x,v,t):
    part1 = sp.erfc((x-(v*t)/(2*np.sqrt(beta*v*t))))
    part2 = sp.exp((v*x)/(beta*v))
    part3 = sp.erfc((x+(v*t)/(2*np.sqrt(beta*v*t))))
    conc = 0.5(part1+(part2*part3))
    return conc

def plot_output(t,conc,conc2):
    mpl.close('all')
    mpl.figure()
    mpl.plot(t,c,linewidth=2,label='Data')
    mpl.plot(t,c2,linewidth=1,label='Guess')
    mpl.legend(frameon=False)
    mpl.xlabel('time (d)')
    mpl.ylabel('Concentration (-)')

def main():
    data_path = ".\\python task\\"
    search_files(data_path)
    print(x)
    
if __name__ == '__main__':
    main()
    
    
