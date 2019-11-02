def plot_mean_beta():
        import numpy as np
        import matplotlib.pyplot as mpl
        dir = r'E:\Zohaib\fiverr\my-task\sami\python-task\my-output'
        datafile =['SummaryA.dat','SummaryF.dat','SummaryK.dat']
        for i in datafile:
            fig_file = 'mean'+i.split('.')[0]+'.png'
            fname = dir + '\\'+fig_file
            fig_dir = dir+'\\'+'mean'+fig_file
            array = np.genfromtxt(fname, skip_header=3)
            #print(temp.shape)
            x_mean = array[:,:6].mean(axis=1)
            #print(x_mean)
            betafit_mean = array[:,18:].mean(axis=1)
            mpl.plot(array[:,0],array[:,18],'bo',label='Model-1',alpha = 0.3)
            mpl.plot(array[:,1],array[:,19],'ro',label='Model-2',alpha = 0.3)
            mpl.plot(array[:,2],array[:,20],'go',label='Model-3',alpha = 0.3)
            mpl.plot(array[:,3],array[:,21],'co',label='Model-4',alpha = 0.3)
            mpl.plot(array[:,4],array[:,22],'mo',label='Model-5',alpha = 0.3)
            mpl.plot(array[:,5],array[:,23],'yo',label='Model-6',alpha = 0.3)
            mpl.plot(x_mean,betafit_mean,'ko',label = 'Mean-Beta', alpha = 0.3)
            mpl.legend()
            mpl.xlabel('distance,x (m)')
            mpl.ylabel('Beta(m)')
            mpl.title(fig_dir.split('y')[1]+'Scenario')
            mpl.savefig(fig_dir)




def plot_scenario(datafile,fig_file):
    import numpy as np
    import matplotlib.pyplot as mpl
    dir = r'E:\Zohaib\fiverr\my-task\sami\python-task\my-output'
    fname = dir + '\\' + datafile
    fig_dir = dir+'\\'+fig_file
    array = np.genfromtxt(fname, skip_header=3)
    #print(temp.shape)
    x_mean = array[:,:6].mean(axis=1)
    #print(x_mean)
    betafit_mean = array[:,18:].mean(axis=1)
    #print(betafit_mean)
    print('printing scenario report..')
    mpl.close('all')
    mpl.figure()
    mpl.plot(array[:,0],array[:,18],'bo',label='Model-1',alpha = 0.3)
    mpl.plot(array[:,1],array[:,19],'ro',label='Model-2',alpha = 0.3)
    mpl.plot(array[:,2],array[:,20],'go',label='Model-3',alpha = 0.3)
    mpl.plot(array[:,3],array[:,21],'co',label='Model-4',alpha = 0.3)
    mpl.plot(array[:,4],array[:,22],'mo',label='Model-5',alpha = 0.3)
    mpl.plot(array[:,5],array[:,23],'yo',label='Model-6',alpha = 0.3)
    mpl.legend()
    mpl.xlabel('distance,x (m)')
    mpl.ylabel('Beta(m)')
    mpl.title(fig_file.split('y')[1]+'Scenario')
    mpl.savefig(fig_dir)
    #plot_mean_beta()
    #mpl.show()
    
   