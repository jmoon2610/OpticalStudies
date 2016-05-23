import samweb_client as sw
import os

samweb = sw.SAMWebClient(experiment='uboone')

x = 6120

while x < 6340:

    arg1 = "run_number = %i and (ub_project.stage = mergeext_unbiased or ub_project.stage = mergebnb_unbiased or ub_project.stage = nubnb_unbiased)" %(x)
    rawData = samweb.listFilesSummary(arg1)
    num_events = rawData['total_event_count']

    if type(num_events) != int:
        sys_out2 = "sed -i -e 's/runnum_%i/runnum_%i/g' SingleRunGain.xml"%(x,x+1) 
        os.system(sys_out2)
        x+=1
        continue


    sys_out="samweb create-definition runnum_%i 'run_number = %i and (ub_project.stage = mergeext_unbiased or ub_project.stage = mergebnb_unbiased or ub_project.stage = nubnb_unbiased)'" %(x,x)
    os.system(sys_out)

    os.system("project.py --xml /uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SingleRunGain.xml --stage RunSingleGain --clean")
    os.system("project.py --xml /uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SingleRunGain.xml --stage RunSingleGain --submit")

    sys_out2 = "sed -i -e 's/runnum_%i/runnum_%i/g' SingleRunGain.xml"%(x,x+1) 
    os.system(sys_out2)

    x+=1
