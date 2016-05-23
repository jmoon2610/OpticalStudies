#include<ctime>
#include<iostream>
#include<iomanip>
#include<fstream>
#include "TROOT.h"
#include "TRint.h"
#include <vector>

void RunFits()
{
  gROOT->ProcessLine(".L /uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SimpleCalibrationFit.C");

  string line;
  std::vector<string> SPE_filepaths;
  ifstream myfile ("/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/SingleRunGain_TreePath.txt");
  if (myfile.is_open())
    {
      while ( getline (myfile,line) )
	{
	  SPE_filepaths.push_back(line);
	}
      myfile.close();
    }

  int CHANNELS = 32;

    
    
  for (unsigned int i = 0; i<SPE_filepaths.size(); i++){

    std::string current_run = SPE_filepaths[i].std::substr(54,4);

    char buffer1[200];
    char buffer2[200];
    sprintf(buffer1,"/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/gains/runnum_%s_gains.txt",current_run.c_str());
    sprintf(buffer2,"/uboone/app/users/moon/OpticalStudies/v05_01_01/workdir/GainsDatabase/RunHistory/gains_sigma/runnum_%s_gains_sig.txt",current_run.c_str());
      
    std::ofstream output_file1(buffer1);
    std::ofstream output_file2(buffer2);


    int current_channel = 0;

    std::vector<double> SPE;

    while (current_channel < CHANNELS) {

      SPE = SimpleCalibrationFit(SPE_filepaths[i].c_str(),current_channel);

      output_file1 << SPE[0] << "\n";
      output_file2 << SPE[1] << "\n";

      current_channel++;

    }
    
    std::ofstream output_file1.close();
    std::ofstream output_file2.close();

  }

}




