# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import os 
import scipy.special as sp
import scipy as spx
import scipy.optimize as op
import matplotlib.pyplot as mpl
from sklearn.metrics import mean_squared_error 

def ob(beta,x,v,t):    
    pos_beta = beta
    part1 = sp.erfc((x-(v*t)/(2.*np.sqrt(pos_beta*v*t))))
    part2 = np.exp((v*x)/(pos_beta*v))
    part3 = sp.erfc((x+(v*t)/(2.*np.sqrt(pos_beta*v*t))))
    conc = 0.5*(part1+(part2*part3))
    print(f'calculted conc = {conc}')
    return conc

def rmse(beta,x,v,t,c):
    
    c2 = ob(beta,x,v,t)
    rm = np.sqrt(np.square(c-c2).mean() )
    #rm =np.sqrt( mean_squared_error(c,c2)) 
    print(f'calculated rm = {rm}')
    return rm       

def opt_beta(beta,x,v,t,c):
    out = op.minimize(rmse,beta,args=(x,v,t,c),method = 'Nelder-Mead', options = {'xatol':1e-10,'disp':False })
    #out = op.fmin_slsqp(rmse, beta,args=(x,v,t,c),acc = 1e-6,epsilon=1.4901161193847656e+01)
    #bnds = ((0.01,None),)
    #out = op.minimize(rmse, beta,args=(x,v,t,c), method='TNC', tol=1e-300)
    print(out.x)
    return out.x



def plot_output(t,conc,conc2,conc3):
    print('inside plot')
    mpl.close('all')
    mpl.figure()
    mpl.plot(t,conc,linewidth=2,label='Data')
    mpl.plot(t,conc2,linewidth=1,label='Guess')
    mpl.plot(t,conc3,linewidth=1,label='fit')
    mpl.legend(frameon=False)
    mpl.xlabel('time (d)')
    mpl.ylabel('Concentration (-)')
    mpl.show()



def main():
    print("++++++++++Main+++++++++++++")
    data_path = ".\\python-task\\"
    beta = 0.5
#     f= "D:\\Zohaib\\Fivrr\\sami\\python-task\\A\\01\\HeatSolo.observation_well_conc.005.solute.dat"
#     data = np.genfromtxt(f,skip_header=2)
#     x= data[0,2]
#     t= data[:,0]/86400
#     c= data[:,1]
#     print(c)
#     arrpos = np.argmax(c>0.5)
#     v=x/t[arrpos]
#     c2 = ob(beta,x,v,t)
#     print(f'calculated c2 = {c2}')
#     betafit = opt_beta(beta,x,v,t,c)
#     c3 = ob(betafit,x,v,t)
#     print(f'calculated c3 ={c3}')
#     plot_output(t,c,c2,c3)
# 


    for subdirs,dirs,files in os.walk(data_path):  
       for i in subdirs:
        print(i) 
        for fname in files: 
                print('++++++++inside for+++++++++')
                print(subdirs)
                f = subdirs+'\\'+fname
                data = np.genfromtxt(f,skip_header=2)
                x= data[0,2]
                t= data[:,0]/86400
                print(t)
                c= data[:,1]
                print(c)
                arrpos = np.argmax(c>0.5)
                v=x/t[arrpos]
                c2 = ob(beta,x,v,t)
                betafit = opt_beta(beta,x,v,t,c)
                c3 = ob(betafit,x,v,t)
                plot_output(t,c,c2,c3)

    
    
if __name__ == '__main__':
    main()
    
