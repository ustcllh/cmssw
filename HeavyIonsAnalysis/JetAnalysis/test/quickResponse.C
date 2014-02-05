

{

  new TFile("HiForest.root");

  akVs5PFJetAnalyzer->cd();
  t->AddFriend("hiEvtAnalyzer/HiTree");

  new TCanvas();

  t->Draw("jtpt/refpt:refpt","hiBin < 4 && abs(refeta) < 3 && refpt > 0","colz");
  t->Draw("jtpt/refpt:refpt","hiBin < 4 && abs(refeta) < 3 && refpt > 0","prof same");

  new TCanvas();

  t->Draw("jtpt/refpt:hiBin","refpt > 30 && abs(refeta) < 3 && refpt > 0","colz");
  t->Draw("jtpt/refpt:hiBin","refpt > 30 && abs(refeta) < 3 && refpt > 0","prof same");


}

