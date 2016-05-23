std::vector<double> SimpleSinglesFit(TString input_filename,int channel_num) {

  gROOT->Reset();
  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);

  TString input_tree_name = "specalib/eventtree";                        // Whatever the tree from the swizzler is called
    

  TFile* in_file = new TFile(input_filename.Data());                     // Get input file output from swizzler
  TTree* in_tree = (TTree*)in_file->Get(input_tree_name);                // Get tree with PMT waveforms and data from input file


  TH1F* singles_histo = new TH1F("singles_histo","Fires in Window",20,0,20);

  char buffer[100];
  sprintf(buffer,"nchfires[%i]",channel_num);

  
  in_tree->Project("singles_histo",buffer,"","goff",in_tree->GetEntries());
  

  double mu = singles_histo->GetMean(1);
  double mu_sig = singles_histo->GetRMS(1);

  std::vector<double> output;

  output.push_back(mu);
  output.push_back(mu_sig);

  in_file->Close();

  return output;

}
