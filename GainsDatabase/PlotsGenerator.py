import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
    

def GetLinFitCoeffs(x,y):

    A = np.vstack([x,np.ones(len(x))]).T
    m,c = np.linalg.lstsq(A,y)[0]
    
    return m
    

    

runs_list = []
gains = [[] for _ in range(32)]
errors = [[] for _ in range(32)]

for files in os.listdir("/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/gains"):

    ch=0
    current_file = "/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/gains/%s"%(files)
    with open(current_file) as infile:
        for line in infile:
            
            gains[ch].append(float(line.rstrip('\n')))
            ch+=1
    
    runs_list.append(int(files[7:11]))


'''
for files in os.listdir("/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/gains_sigma"):

    ch=0
    current_file = "/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/gains_sigma/%s"%(files)
    with open(current_file) as infile:
        for line in infile:

            if float(line.rstrip('\n'))==0: 
                errors[ch].append(1)
                ch+=1

            else:
                errors[ch].append(float(line.rstrip('\n')))
                ch+=1
'''


for x in range(32):

    print "Channel %i"%(x) , " " , GetLinFitCoeffs(runs_list,gains[x])
    

    
no_zero = gains[1]
runs_list_tmp = runs_list

while 0 in no_zero:
    loc = no_zero.index(0)
    no_zero.pop(loc)
    runs_list_tmp.pop(loc)

print GetLinFitCoeffs(runs_list,no_zero)




#    print "Channel %i"%(x) , " " , GetLinFitCoeffs(runs_list,no_zero)


#plt.plot(runs_list,gains[15],'ro',ms=3)           
#plt.errorbar(runs_list,gains[5],errors[5],xerr=None,ls='none',marker='o')
#plt.axis([5500,6000,10,35])

#plt.hist(gains[15],bins=20,range=(18,24))


#fig.suptitle('Gains \n Run Ranges  %s , %s , %s , %s \n Date Ranges %s , %s , %s , %s'%(run_list[3],run_list[2],run_list[1],run_list[0],date_list[3],date_list[2],date_list[1],date_list[0]),fontsize=12,fontweight='bold',y=1.0)


#plt.savefig('/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/bla.png',figsize=(8.6),dpi=300)

