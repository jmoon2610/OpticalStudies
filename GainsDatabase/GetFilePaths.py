import os


os.system("rm /uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SingleRunGain_TreePath.txt")

os.system("find /pnfs/uboone/scratch/users/moon/SingleRunGains/runnum_6120/*/ -name 'SPEcalibration_output.root' > /uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SingleRunGain_TreePath.txt")

x=6121
while x < 6340:

    sys_arg = "find /pnfs/uboone/scratch/users/moon/SingleRunGains/runnum_%i/*/ -name 'SPEcalibration_output.root' >> /uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SingleRunGain_TreePath.txt"%(x)
    
    os.system(sys_arg)

    x+=1

