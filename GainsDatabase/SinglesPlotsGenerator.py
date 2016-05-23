import numpy as np
import matplotlib.pyplot as plt
import os
    

def GetLinFitCoeffs(x,y):

    A = np.vstack([x,np.ones(len(x))]).T
    m,c = np.linalg.lstsq(A,y)[0]
    
    return m
    


runs_list = []
singles = [[] for _ in range(32)]
errors = [[] for _ in range(32)]

for files in os.listdir("/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/singles"):

    ch=0
    current_file = "/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/singles/%s"%(files)
    with open(current_file) as infile:
        for line in infile:
            
            singles[ch].append(42.662*float(line.rstrip('\n')))
            ch+=1
    
    runs_list.append(int(files[7:11]))

'''
for files in os.listdir("/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/singles_sigma"):

    ch=0
    current_file = "/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/singles_sigma/%s"%(files)
    with open(current_file) as infile:
        for line in infile:

            errors[ch].append(float(line.rstrip('\n')))
            ch+=1
'''

#for x in range(32):
#    print GetLinFitCoeffs(runs_list,gains[x])
    

#plt.errorbar(runs_list,singles[5],errors[5],xerr=None,ls='none',marker='o',markersize='2',capsize=1)
plt.plot(runs_list,singles[27],'ro',ms=3)           
plt.axis([5500,6000,0,450])


plt.savefig('/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/bla.png',figsize=(8.6),dpi=300)

