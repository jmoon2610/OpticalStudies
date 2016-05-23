import ROOT
from ROOT import *
from array import array
import os

outfile = ROOT.TFile("GainsHistory.root","recreate")
outtree = ROOT.TTree("gains_tree","gains_tree")

runnum       = array('i',[0])
readoutch    = array('i',[0])
gain         = array('f',[0])
gain_sig     = array('f',[0])
singles_rate = array('f',[0])
singles_sig  = array('f',[0])

outtree.Branch('runnum'       , runnum       , 'runnum/I')
outtree.Branch('readoutch'    , readoutch    , 'readoutch/I')
outtree.Branch('gain'         , gain         , 'gain/F')
outtree.Branch('gain_sig'     , gain_sig     , 'gain_sig/F')
outtree.Branch('singles_rate' , singles_rate , 'singles_rate/F')
outtree.Branch('singles_sig'  , singles_sig  , 'singles_sig/F')

gains_dict       = {}
gains_sig_dict   = {}
singles_dict     = {}
singles_sig_dict = {}

for fil in os.listdir("RunHistory/gains"):

    file_name = "RunHistory/gains/%s"%(fil)
    run_number = int(fil[7:11])

    with open(file_name) as infile:
        gain_list = infile.readlines()

    gain_list = [x.strip('\n') for x in gain_list]

    gains_dict[run_number] = gain_list


for fil in os.listdir("RunHistory/gains_sigma"):

    file_name = "RunHistory/gains_sigma/%s"%(fil)
    run_number = int(fil[7:11])

    with open(file_name) as infile:
        gain_sig_list = infile.readlines()

    gain_sig_list = [x.strip('\n') for x in gain_sig_list]

    gains_sig_dict[run_number] = gain_sig_list


for fil in os.listdir("RunHistory/singles"):

    file_name = "RunHistory/singles/%s"%(fil)
    run_number = int(fil[7:11])

    with open(file_name) as infile:
        singles_list = infile.readlines()

    singles_list = [x.strip('\n') for x in singles_list]

    singles_dict[run_number] = singles_list


for fil in os.listdir("RunHistory/singles_sigma"):

    file_name = "RunHistory/singles_sigma/%s"%(fil)
    run_number = int(fil[7:11])

    with open(file_name) as infile:
        singles_sig_list = infile.readlines()

    singles_sig_list = [x.strip('\n') for x in singles_sig_list]

    singles_sig_dict[run_number] = singles_sig_list


for run in gains_dict:

    if gains_dict[run].count(0)>0 or gains_sig_dict[run].count(0)>0 or singles_dict[run].count(0)>0 or singles_sig_dict[run].count(0)>0:
        continue

    for ch in xrange(32):
        
        runnum[0]       = int(run)
        readoutch[0]    = ch
        gain[0]         = float(gains_dict[run][ch])
        gain_sig[0]     = float(gains_sig_dict[run][ch])
        singles_rate[0] = float(singles_dict[run][ch])
        singles_sig[0]  = float(singles_sig_dict[run][ch])
                                                        
        outtree.Fill()

outfile.Write()
                                                       
                                                          
