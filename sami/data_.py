import numpy as np
import os 
import scipy.special as sp
import scipy.optimize as op
import matplotlib.pyplot as mpl
from sklearn.metrics import mean_squared_error 
import math
import report as dt


def ob(beta,x,v,t):    
    pos_beta = beta
    part1 = sp.erfc((x-(v*t)/(2.*np.sqrt(pos_beta*v*t))))
    part2 = np.exp((v*x)/(pos_beta*v))
    part3 = sp.erfc((x+(v*t)/(2.*np.sqrt(pos_beta*v*t))))
    conc = (0.5*(part1+part2*part3))*1e300
    #print(f'calculted conc = {conc}')
    return conc

def rmse(beta,x,v,t,c):
    
    c2 = ob(beta,x,v,t)/1e300
    c = c/1e300
    rm = np.sqrt(np.average(np.square(c-c2)))
    #rm =np.sqrt(mean_squared_error(c,c2)).astype('float64') 
    print(f'calculated rm = {rm}')
    return rm       

def opt_beta(beta,x,v,t,c):
    out = op.minimize(rmse,beta,args=(x,v,t,c),method = 'Nelder-Mead', options = {'xatol':1e-6,'disp':False})
    #out = op.fmin_slsqp(rmse, beta,args=(x,v,t,c),acc = 1e-6,epsilon=1.4901161193847656e+01)
    #bnds = ((0.01,None),)
    #out = op.minimize(rmse, beta,args=(x,v,t,c), method='TNC', tol=1e-300)
    #print(out.x)
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

# def plot_scenario(x,beta):
#     print('printing scenario report..')
#     mpl.close('all')
#     mpl.figure()
#     mpl.plot(x,beta,'bo',label='data')
#     # mpl.plot(t,conc2,linewidth=1,label='Guess')
#     # mpl.plot(t,conc3,linewidth=1,label='fit')
#     # mpl.legend(frameon=False)
#     mpl.xlabel('distance,x (m)')
#     mpl.ylabel('Beta(m)')
#     mpl.show()



def main():
    print("Main")
    beta = np.array([1.])
    folder = [r'\A',r'\F',r'\Kshort']
    folderpart1 = r'E:\Zohaib\Fiverr\my-task\sami\python-task'
    folderpart2 = [r'\01',r'\02',r'\03',r'\04',r'\05',r'\06']
    outfolder = r'E:\Zohaib\Fiverr\my-task\sami\python-task\my-output'
    allfiles = os.listdir(r'.\python-task\A\01')
    xs = np.zeros((len(allfiles),len(folderpart2)))
    ys = np.zeros((len(allfiles),len(folderpart2)))
    vs = np.zeros((len(allfiles),len(folderpart2)))
    betasout = np.zeros((len(allfiles),len(folderpart2)))
    for i in range(0, len(folder)):
        fnameout1 = 'Summary'+folder[i].split('\\')[1]+'.dat'
        fnameout2 = 'Summary'+folder[i].split('\\')[1]+'.png'
        for j in range(0, len(folderpart2)):
            allfiles = os.listdir(folderpart1+folder[i]+folderpart2[j])
            fullpath = folderpart1+folder[i]+folderpart2[j]
            os.chdir(fullpath)  
            #print(fullpath)
            for k in range(0,len(allfiles)):
                data = np.genfromtxt(allfiles[k],skip_header=2)
                x= data[0,2]
                t= data[:,0]/86400.
                c= data[:,1]*1e300
                arrpos = np.argmax(c>0.5)
                v=x/t[arrpos]
                y = data[0,3]
                c2 = ob(beta,x,v,t)
                #print(f'calculated c2 = {c2}')
                betafit = opt_beta(beta,x,v,t,c)
                #print(f'betafit = {betafit}')
                c3 = ob(betafit,x,v,t)
                #print(f'calculated c3 ={c3}')
                plot_output(t,c,c2,c3)
                xs[k][j] = x
                ys[k][j] = y
                # ys_m = ys.mean()
                vs[k][j] = v
                betasout[k][j] = betafit
                
                #plot_output(t,c,c2,c3)
            
        data_out = np.column_stack((xs,ys,vs,betasout))
        headertxt  = 'Scenario Kshort\n'
        headertxt += '1,2,3,4,5,6'*6+'\n'
        headertxt += 'Xs, '*6+'Ys, '*6+'Vs, '*6+'betafit, '*6+'\n'
        np.savetxt(outfolder+'\\'+fnameout1,data_out,fmt=('%.1f','%.1f','%.1f','%.1f','%.1f','%.1f',
                                                            '%.1f','%.1f','%.1f','%.1f','%.1f','%.1f',
                                                            '%.1f','%.1f','%.1f','%.1f','%.1f','%.1f',
                                                            '%.2e','%.2e','%.2e','%.2e','%.2e','%.2e',  
                                                            ), header=headertxt)
        dt.plot_scenario(fnameout1,fnameout2)




    # f= ".\\python-task\\A\\01\\HeatSolo.observation_well_conc.005.solute.dat"
    # data = np.genfromtxt(f,skip_header=2)
    # x= data[0,2]
    # t= data[:,0]/86400.
    # c= data[:,1]*1e300
    # arrpos = np.argmax(c>0.5)
    # v=x/t[arrpos]
    # #c2 = ob(beta,x,v,t)
    # #print(f'calculated c2 = {c2}')
    # betafit = opt_beta(beta,x,v,t,c)
    # print(f'betafit = {betafit}')
    # c3 = ob(betafit,x,v,t)
    # print(f'calculated c3 ={c3}')
    # plot_output(t,c,c3)



    # for subdirs,dirs,files in os.walk(data_path):  
    #    for i in subdirs:
    #     print(i) 
    #     for fname in files: 
    #             print('++++++++inside for+++++++++')
    #             print(subdirs)
    #             f = subdirs+'\\'+fname
    #             data = np.genfromtxt(f,skip_header=2)
    #             x= data[0,2]
    #             t= data[:,0]/86400
    #             print(t)
    #             c= data[:,1]
    #             print(c)
    #             arrpos = np.argmax(c>0.5)
    #             v=x/t[arrpos,0]
    #             c2 = ob(beta,x,v,t)
    #             betafit = opt_beta(beta,x,v,t,c)
    #             c3 = ob(betafit,x,v,t)
    #             plot_output(t,c,c2,c3)

    
    
if __name__ == '__main__':
    main()
    
