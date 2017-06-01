// -*- C++ -*-
//
// Package:    HiJetBackground/HiFJRhoFlowModulationProducer
// Class:      HiFJRhoFlowModulationProducer

//ROOT dependencies
#include "TMath.h"
#include "TF1.h"
#include "TH1F.h"
#include "TCanvas.h"
#include "TLine.h"
#include "TFile.h"
#include "TNamed.h"
#include "TStyle.h"

#include <cmath>

#include "RecoHI/HiJetAlgos/plugins/HiFJRhoFlowModulationProducer.h"
using namespace std;
using namespace edm;

HiFJRhoFlowModulationProducer::HiFJRhoFlowModulationProducer(const edm::ParameterSet& iConfig)
{
  pfCandsToken_ = consumes<reco::PFCandidateCollection>(iConfig.getParameter<edm::InputTag>( "pfCandSource" ));
  mapRhoToken_ = consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>( "mapToRho" ));
  mapRhoMToken_ = consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>( "mapToRhoM" ));
  jetsToken_ = consumes<edm::View<reco::Jet> >(iConfig.getParameter<edm::InputTag>( "jetSource" ));

  //register your products
  produces<std::vector<double> >("rhoFlowFitParams");
}


HiFJRhoFlowModulationProducer::~HiFJRhoFlowModulationProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

// ------------ method called to produce the data  ------------
void
HiFJRhoFlowModulationProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  //Values from rho calculator 
  edm::Handle<std::vector<double>> mapRho;
  iEvent.getByToken(mapRhoToken_, mapRho);

  edm::Handle<std::vector<double>> mapRhoM;  
  iEvent.getByToken(mapRhoMToken_, mapRhoM);

  edm::Handle<reco::PFCandidateCollection> pfCands;
  iEvent.getByToken(pfCandsToken_, pfCands);

  const reco::PFCandidateCollection *pfCandidateColl_p = pfCands.product();

  double eventPlane2Cos = 0;
  double eventPlane2Sin = 0;

  double eventPlane3Cos = 0;
  double eventPlane3Sin = 0;

  double eventPlane2CosWeight = 0;
  double eventPlane2SinWeight = 0;

  double eventPlane3CosWeight = 0;
  double eventPlane3SinWeight = 0;

  std::auto_ptr<std::vector<double> > rhoFlowFitParamsOut(new std::vector<double>(7,1e-6));

  rhoFlowFitParamsOut->at(0) = mapRho->at(4);
  rhoFlowFitParamsOut->at(1) = 0;
  rhoFlowFitParamsOut->at(2) = 0;
  rhoFlowFitParamsOut->at(3) = 0;
  rhoFlowFitParamsOut->at(4) = 0;


  bool isGoodFill = false;
  int nFill = 0;

  for(unsigned pfIter = 0; pfIter < pfCandidateColl_p->size(); pfIter++){
    const reco::PFCandidate pfCandidate = pfCandidateColl_p->at(pfIter);

    if(pfCandidate.eta() < -1.0) continue;
    if(pfCandidate.eta() > 1.0) continue;

    if(pfCandidate.pt() < .2) continue;
    if(pfCandidate.pt() > 10.) continue;

    if(pfCandidate.particleId() != 1) continue;

    isGoodFill = true;
    nFill++;

    eventPlane2Cos += std::cos(2*pfCandidate.phi());
    eventPlane2Sin += std::sin(2*pfCandidate.phi());

    eventPlane3Cos += std::cos(3*pfCandidate.phi());
    eventPlane3Sin += std::sin(3*pfCandidate.phi());

    eventPlane2CosWeight += pfCandidate.pt()*std::cos(2*pfCandidate.phi());
    eventPlane2SinWeight += pfCandidate.pt()*std::sin(2*pfCandidate.phi());

    eventPlane3CosWeight += pfCandidate.pt()*std::cos(3*pfCandidate.phi());
    eventPlane3SinWeight += pfCandidate.pt()*std::sin(3*pfCandidate.phi());
  }

  if(isGoodFill){
    const int nPhiBins = std::fmax(10, nFill/30);

    std::string name = "phiTestIEta4_rho" + std::to_string(int(mapRho->at(4))) + "_" + std::to_string(iEvent.id().event()) + "_h";
    std::string nameWeight = "phiWeightTestIEta4_rho" + std::to_string(int(mapRho->at(4))) + "_" + std::to_string(iEvent.id().event()) + "_h";

    TH1F* phi_h = new TH1F(name.c_str(), ";#phi;Track counts (.2 < p_{T} < 10)", nPhiBins, -TMath::Pi(), TMath::Pi());
    TH1F* phiWeight_h = new TH1F(nameWeight.c_str(), ";#phi;Tracks w/ p_{T} weight (.2 < p_{T} < 10)", nPhiBins, -TMath::Pi(), TMath::Pi());

    for(unsigned pfIter = 0; pfIter < pfCandidateColl_p->size(); pfIter++){
      const reco::PFCandidate pfCandidate = pfCandidateColl_p->at(pfIter);

      if(pfCandidate.eta() < -1.0) continue;
      if(pfCandidate.eta() > 1.0) continue;

      if(pfCandidate.pt() < .3) continue;
      if(pfCandidate.pt() > 3.) continue;

      if(pfCandidate.particleId() != 1) continue;

      phi_h->Fill(pfCandidate.phi());
      phiWeight_h->Fill(pfCandidate.phi(), pfCandidate.pt());
    }

    double eventPlane2 = std::atan2(eventPlane2Sin, eventPlane2Cos)/2.;
    double eventPlane3 = std::atan2(eventPlane3Sin, eventPlane3Cos)/3.;

    rhoFlowFitParamsOut->at(2) = eventPlane2;
    rhoFlowFitParamsOut->at(4) = eventPlane3;

    //    double eventPhi2Weight = std::atan2(eventPlane2SinWeight, eventPlane2CosWeight)/2.;
    //    double eventPhi3Weight = std::atan2(eventPlane3SinWeight, eventPlane3CosWeight)/3.;
    
    std::string flowFitForm = "[0]*(1 + 2*([1]*TMath::Cos(2*(x - " + std::to_string(eventPlane2) + ")) + [2]*TMath::Cos(3*(x - " + std::to_string(eventPlane3) + "))))";

    TF1* flowFit_p = new TF1("flowFit", flowFitForm.c_str(), -TMath::Pi(), TMath::Pi());
    flowFit_p->SetParameter(0, mapRho->at(4));
    flowFit_p->SetParameter(1, 0);
    flowFit_p->SetParameter(2, 0);

    TF1* lineFit_p = new TF1("lineFit", "[0]", -TMath::Pi(), TMath::Pi());
    lineFit_p->SetParameter(0, mapRho->at(4));

    std::string flowFitForm2 = std::to_string(mapRho->at(4)) + "*(1 + 2*([0]*TMath::Cos(2*(x - " + std::to_string(eventPlane2) + ")) + [1]*TMath::Cos(3*(x - " + std::to_string(eventPlane3) + "))))";

    TF1* flowFit2_p = new TF1("flowFit2", flowFitForm2.c_str(), -TMath::Pi(), TMath::Pi());
    flowFit2_p->SetParameter(1, 0);
    flowFit2_p->SetParameter(2, 0);
    flowFit2_p->SetMarkerColor(kBlue);
    flowFit2_p->SetLineColor(kBlue);


    for(int binIter = 0; binIter < phi_h->GetNbinsX(); binIter++){
      phi_h->SetBinContent(binIter+1, phi_h->GetBinContent(binIter+1)/phi_h->GetBinWidth(binIter+1));
      phi_h->SetBinError(binIter+1, phi_h->GetBinError(binIter+1)/phi_h->GetBinWidth(binIter+1));
    }

    for(int binIter = 0; binIter < phiWeight_h->GetNbinsX(); binIter++){
      phiWeight_h->SetBinContent(binIter+1, phiWeight_h->GetBinContent(binIter+1)/phiWeight_h->GetBinWidth(binIter+1));
      phiWeight_h->SetBinError(binIter+1, phiWeight_h->GetBinError(binIter+1)/phiWeight_h->GetBinWidth(binIter+1));
    }

    phi_h->Fit(flowFit_p, "Q M E", "", -TMath::Pi(), TMath::Pi());
    phi_h->Fit(flowFit2_p, "Q M E", "", -TMath::Pi(), TMath::Pi());

    phiWeight_h->Fit(flowFit_p, "Q M E", "", -TMath::Pi(), TMath::Pi());
    phiWeight_h->Fit(flowFit2_p, "Q M E", "", -TMath::Pi(), TMath::Pi());
    phiWeight_h->Fit(lineFit_p, "Q M E", "", -TMath::Pi(), TMath::Pi());

    rhoFlowFitParamsOut->at(0) = flowFit_p->GetParameter(0);
    rhoFlowFitParamsOut->at(1) = flowFit_p->GetParameter(1);
    rhoFlowFitParamsOut->at(3) = flowFit_p->GetParameter(2);
    
    rhoFlowFitParamsOut->at(5) = flowFit_p->GetChisquare()/float(nPhiBins-3);
    rhoFlowFitParamsOut->at(6) = lineFit_p->GetChisquare()/float(nPhiBins-1);

    delete phi_h;
    delete phiWeight_h;

    delete flowFit_p;
    delete lineFit_p;
    delete flowFit2_p;
  }

  iEvent.put(rhoFlowFitParamsOut, "rhoFlowFitParams");
}


// ------------ method called once each job just before starting event loop  ------------
void 
HiFJRhoFlowModulationProducer::beginJob()
{

}

// ------------ method called once each job just after ending the event loop  ------------
void 
HiFJRhoFlowModulationProducer::endJob() {
}
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void HiFJRhoFlowModulationProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(HiFJRhoFlowModulationProducer);

