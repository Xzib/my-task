import numpy as np
fname = r'D:\Zohaib\Fivrr\sami\python-task\my-output\SummaryK.dat'
temp = np.genfromtxt(fname, skip_header=3)
print(temp.shape)