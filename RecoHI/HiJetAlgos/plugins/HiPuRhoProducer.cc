// -*- C++ -*-
//
// Package:    HiJetBackground/HiPuRhoProducer
// Class:      HiPuRhoProducer
// 
/**\class HiPuRhoProducer HiPuRhoProducer.cc HiJetBackground/HiPuRhoProducer/plugins/HiPuRhoProducer.cc

 Description: Producer to dump Pu-jet style rho into event content

 Implementation:
 Just see MultipleAlgoIterator - re-implenting for use in CS jet with sigma subtraction and zeroing
*/
//
// Original Author:  Chris McGinn - in Style of HiFJRhoProducer
//         Created:  Mon, 29 May 2017
//
//

#include <memory>
#include <string>

#include "TMath.h"

#include "RecoHI/HiJetAlgos/plugins/HiPuRhoProducer.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/isFinite.h"

#include "Geometry/Records/interface/CaloGeometryRecord.h"

using namespace edm;
using namespace pat;

//using ival = boost::icl::interval<double>;

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
HiPuRhoProducer::HiPuRhoProducer(const edm::ParameterSet& iConfig) : 
  dropZeroTowers_(iConfig.getUntrackedParameter<bool>("dropZeroTowers",true)),
  nSigmaPU_(iConfig.getParameter<double>("nSigmaPU")),
  radiusPU_(iConfig.getParameter<double>("radiusPU")),
  rParam_(iConfig.getParameter<double>("rParam")),
  src_(iConfig.getParameter<edm::InputTag>("src"))
{
  if(iConfig.exists("puPtMin")) puPtMin_ = iConfig.getParameter<double>("puPtMin");
  else{
    puPtMin_ = 10;
    edm::LogWarning("MisConfiguration")<<"the parameter puPtMin is now necessary for PU substraction. setting it to "<<puPtMin_;
  }

  if(iConfig.exists("minimumTowersFraction")){
    minimumTowersFraction_ = iConfig.getParameter<double>("minimumTowersFraction");
    std::cout << "LIMITING THE MINIMUM TOWERS FRACTION TO: " << minimumTowersFraction_ << std::endl;
  }
  else{
    minimumTowersFraction_ = 0;
    std::cout<< "ATTENTION - NOT LIMITING THE MINIMUM TOWERS FRACTION" << std::endl;
  }

  input_candidateview_token_ = consumes<reco::CandidateView>(src_);

  etaEdgeLow_.reserve(nEtaTow_);
  etaEdgeHi_.reserve(nEtaTow_);
  etaEdges_.reserve(nEtaTow_+1);
  rho_.reserve(nEtaTow_);
  rhoM_.reserve(nEtaTow_);

  const double etatow[42] = {0.000, 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.500, 2.650, 2.853, 3.000, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191};

  for(int i=0;i<42;i++){
    etaedge[i]=etatow[i];
  }

  //register your products
  produces<std::vector<double> >("mapEtaEdges");
  produces<std::vector<double> >("mapToRho");
  produces<std::vector<double> >("mapToRhoM");
}


HiPuRhoProducer::~HiPuRhoProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

// ------------ method called to produce the data  ------------
void HiPuRhoProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  bool debug = false;
  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  setupGeometryMap(iEvent, iSetup);

  etaEdgeLow_.clear();
  etaEdgeHi_.clear();
  etaEdges_.clear();
  rho_.clear();
  rhoM_.clear();

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  inputs_.clear();
  fjInputs_.clear();
  fjJets_.clear();

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  // Get the particletowers
  edm::Handle<reco::CandidateView> inputsHandle;
  iEvent.getByToken(input_candidateview_token_, inputsHandle);

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;
 
  for(size_t i = 0; i < inputsHandle->size(); ++i){
    inputs_.push_back(inputsHandle->ptrAt(i));
  }

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  fjInputs_.reserve(inputs_.size());
  inputTowers();
  fjOriginalInputs_ = fjInputs_;

  calculatePedestal(fjInputs_);
  subtractPedestal(fjInputs_);

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  fjJetDefinition_= JetDefPtr(new fastjet::JetDefinition(fastjet::antikt_algorithm, rParam_));
  fjClusterSeq_ = ClusterSequencePtr(new fastjet::ClusterSequence(fjInputs_, *fjJetDefinition_));
  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;
  fjJets_ = fastjet::sorted_by_pt(fjClusterSeq_->inclusive_jets(puPtMin_));

  //  std::cout << "Inputs: (" << fjInputs_.size() << ")" << std::endl;
  //  std::cout << "JETS: (" << fjJets_.size() << ")" << std::endl;
  //  for(unsigned int iter = 0; iter < fjJets_.size(); ++iter){
  //    std::cout << " " << iter << "/" << fjJets_.size() << ": " << fjJets_.at(iter).pt() << std::endl;
  //  }

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  etaEdgeLow_.clear();
  etaEdgeHi_.clear();
  etaEdges_.clear();
  rho_.clear();
  rhoM_.clear();

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  std::vector<fastjet::PseudoJet> orphanInput;
  calculateOrphanInput(orphanInput);
  calculatePedestal(orphanInput);

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  //  std::cout << "Midrho: " <<  rho_.at(rho_.size()/2) << std::endl;
  packageRho();
  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;
  //  std::cout << "Midrho: " <<  rho_.at(rho_.size()/2) << std::endl;
  putRho(iEvent, iSetup);

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;
}

void HiPuRhoProducer::inputTowers( )
{
  std::vector<edm::Ptr<reco::Candidate> >::const_iterator inBegin = inputs_.begin(),
    inEnd = inputs_.end(), i = inBegin;
  for(; i != inEnd; ++i){
    reco::CandidatePtr input = *i;
    
    if(edm::isNotFinite(input->pt())) continue;
    if(input->pt() < 100*std::numeric_limits<double>::epsilon()) continue;
    
    fjInputs_.push_back(fastjet::PseudoJet(input->px(),input->py(),input->pz(), input->energy()));
    fjInputs_.back().set_user_index(i - inBegin);
  }
}

void HiPuRhoProducer::setupGeometryMap(edm::Event& iEvent,const edm::EventSetup& iSetup)
{

  LogDebug("PileUpSubtractor")<<"The subtractor setting up geometry...\n";

  if(geo_ == 0) {
    edm::ESHandle<CaloGeometry> pG;
    iSetup.get<CaloGeometryRecord>().get(pG);
    geo_ = pG.product();
    std::vector<DetId> alldid =  geo_->getValidDetIds();

    int ietaold = -10000;
    ietamax_ = -10000;
    ietamin_ = 10000;
    for(std::vector<DetId>::const_iterator did=alldid.begin(); did != alldid.end(); did++){
      if((*did).det() == DetId::Hcal){
        HcalDetId hid = HcalDetId(*did);
        if((hid).depth() == 1){
          allgeomid_.push_back(*did);

          if((hid).ieta() != ietaold){
            ietaold = (hid).ieta();
            geomtowers_[(hid).ieta()] = 1;
            if((hid).ieta() > ietamax_) ietamax_ = (hid).ieta();
            if((hid).ieta() < ietamin_) ietamin_ = (hid).ieta();
          }
          else{
            geomtowers_[(hid).ieta()]++;
          }
        }
      }
    }
  }

  for (int i = ietamin_; i<ietamax_+1; i++) {
    ntowersWithJets_[i] = 0;
  }
}


void HiPuRhoProducer::calculatePedestal(std::vector<fastjet::PseudoJet> const & coll)
{
  LogDebug("PileUpSubtractor")<<"The subtractor calculating pedestals...\n";

  std::map<int,double> emean2;
  std::map<int,int> ntowers;

  int ietaold = -10000;
  int ieta0 = -100;

  // Initial values for emean_, emean2, esigma_, ntowers                                                           

  
  for(int vi = 0; vi < nEtaTow_; ++vi){
    int it = vi+1;
    if(it > nEtaTow_/2) it = vi - nEtaTow_;

    int sign = 1;
    if(it < 0){
      sign = -1;
    }
    
    vieta[vi] = it;
    veta[vi] = sign*(etaedge[abs(it)] + etaedge[abs(it)-1])/2.;
    vngeom[vi] = -99;
    vntow[vi] = -99;

    vmean1[vi] = -99;
    vrms1[vi] = -99;
    vrho1[vi] = -99;
    
    if((*(ntowersWithJets_.find(it))).second == 0){
      vmean0[vi] = -99;
      vrms0[vi] = -99;
      vrho0[vi] = -99;
    }
  }

  for(int i = ietamin_; i < ietamax_+1; i++){
    emean_[i] = 0.;
    emean2[i] = 0.;
    esigma_[i] = 0.;
    ntowers[i] = 0;
  }

  for(std::vector<fastjet::PseudoJet>::const_iterator input_object = coll.begin(),
	fjInputsEnd = coll.end();
      input_object != fjInputsEnd; ++input_object){
    
    const reco::CandidatePtr & originalTower= inputs_[ input_object->user_index()];
    ieta0 = ieta(originalTower);
    double Original_Et = originalTower->et();
    //    if(sumRecHits_) Original_Et = getEt(originalTower);
    
    if(ieta0-ietaold != 0){
      emean_[ieta0] = emean_[ieta0]+Original_Et;
      emean2[ieta0] = emean2[ieta0]+Original_Et*Original_Et;
      ntowers[ieta0] = 1;
      ietaold = ieta0;
    }
    else{
      emean_[ieta0] = emean_[ieta0]+Original_Et;
      emean2[ieta0] = emean2[ieta0]+Original_Et*Original_Et;
      ntowers[ieta0]++;
    }
  }

  for(std::map<int,int>::const_iterator gt = geomtowers_.begin(); gt != geomtowers_.end(); gt++){
    int it = (*gt).first;
    int vi = it-1;
    if(it < 0) vi = nEtaTow_ + it;
    
    double e1 = (*(emean_.find(it))).second;
    double e2 = (*emean2.find(it)).second;
    int nt = (*gt).second - (*(ntowersWithJets_.find(it))).second;

    if(vi < nEtaTow_){
      vngeom[vi] = (*gt).second;
      vntow[vi] = nt;
    }

    LogDebug("PileUpSubtractor")<<" ieta : "<<it<<" number of towers : "<<nt<<" e1 : "<<e1<<" e2 : "<<e2<<"\n";
    
    if(nt > 0){
      emean_[it] = e1/nt;
      double eee = e2/nt - e1*e1/(nt*nt);
      if(eee<0.) eee = 0.;
      esigma_[it] = nSigmaPU_*sqrt(eee);

      double etaWidth = etaedge[abs(it)] - etaedge[abs(it)-1];
      if(etaWidth < 0) etaWidth *= -1.;

      int sign = 1;
      if(it < 0){
	sign = -1;
      }
      
      if(double(sign)*etaedge[abs(it)] < double(sign)*etaedge[abs(it)-1]){
	etaEdgeLow_.push_back(double(sign)*etaedge[abs(it)]);
	etaEdgeHi_.push_back(double(sign)*etaedge[abs(it)-1]);
      }
      else{
	etaEdgeHi_.push_back(double(sign)*etaedge[abs(it)]);
	etaEdgeLow_.push_back(double(sign)*etaedge[abs(it)-1]);
      }

      if(vi < nEtaTow_){
	vmean1[vi] = emean_[it];
	vrho1[vi] = emean_[it]/(etaWidth*(2.*3.14159265359/vngeom[vi]));
	rho_.push_back(vrho1[vi]);
	rhoM_.push_back(0);
	vrms1[vi] = esigma_[it];
	if(vngeom[vi] == vntow[vi]){
	  vmean0[vi] = emean_[it];
	  vrho0[vi] = emean_[it]/(etaWidth*(2.*3.14159265359/vngeom[vi]));
	  //	  rho_.push_back(vrho0[vi]);
	  vrms0[vi] = esigma_[it];
	}
      }
    }
    else{
      emean_[it] = 0.;
      esigma_[it] = 0.;
    }
    LogDebug("PileUpSubtractor")<<" ieta : "<<it<<" Pedestals : "<<emean_[it]<<"  "<<esigma_[it]<<"\n";
  }
}


void HiPuRhoProducer::subtractPedestal(std::vector<fastjet::PseudoJet> & coll)
{

  LogDebug("PileUpSubtractor")<<"The subtractor subtracting pedestals...\n";
  int it = -100;
  std::vector<fastjet::PseudoJet> newcoll;

  for(std::vector<fastjet::PseudoJet>::iterator input_object = coll.begin(),
	fjInputsEnd = coll.end();
      input_object != fjInputsEnd; ++input_object){

    reco::CandidatePtr const & itow = inputs_[input_object->user_index()];

    it = ieta(itow);
    iphi(itow);

    double Original_Et = itow->et();
    //    if(sumRecHits_) Original_Et = getEt(itow);

    double etnew = Original_Et - (*(emean_.find(it))).second - (*(esigma_.find(it))).second;
    float mScale = etnew/input_object->Et();
    if(etnew < 0.) mScale = 0.;

    math::XYZTLorentzVectorD towP4(input_object->px()*mScale, input_object->py()*mScale,
				   input_object->pz()*mScale, input_object->e()*mScale);

    int index = input_object->user_index();
    input_object->reset_momentum(towP4.px(),
				 towP4.py(),
				 towP4.pz(),
				 towP4.energy());
    input_object->set_user_index(index);

    if(etnew > 0. && dropZeroTowers_) newcoll.push_back(*input_object);
  }

  if(dropZeroTowers_) coll = newcoll;
}


void HiPuRhoProducer::calculateOrphanInput(std::vector<fastjet::PseudoJet> & orphanInput)
{
  LogDebug("PileUpSubtractor")<<"The subtractor calculating orphan input...\n";
  
  fjInputs_ = fjOriginalInputs_;
  
  std::vector<int> jettowers; // vector of towers indexed by "user_index"                                                
  std::vector<std::pair<int,int> >  excludedTowers; // vector of excluded ieta, iphi values                                   

  std::vector<fastjet::PseudoJet>::iterator pseudojetTMP = fjJets_.begin(),
    fjJetsEnd = fjJets_.end();

  //  cout<<"First iteration found N jets : "<<fjJets_.size()<<endl;                                               

  nref = 0;

  for(; pseudojetTMP != fjJetsEnd; ++pseudojetTMP){
    if(nref < nMaxJets_){
      jtexngeom[nref] = 0;
      jtexntow[nref] = 0;
      jtexpt[nref] = 0;
      jtpt[nref] = pseudojetTMP->perp();
      jteta[nref] = pseudojetTMP->eta();
      jtphi[nref] = pseudojetTMP->phi();
    }
    
    if(pseudojetTMP->perp() < puPtMin_) continue;

    for(std::vector<HcalDetId>::const_iterator im = allgeomid_.begin(); im != allgeomid_.end(); im++){
      double dr = reco::deltaR(geo_->getPosition((DetId)(*im)),(*pseudojetTMP));
      std::vector<std::pair<int,int> >::const_iterator exclude = find(excludedTowers.begin(),excludedTowers.end(),std::pair<int,int>(im->ieta(),im->iphi()));
      if(dr < radiusPU_ && exclude == excludedTowers.end() && (geomtowers_[(*im).ieta()] - ntowersWithJets_[(*im).ieta()]) > minimumTowersFraction_*(geomtowers_[(*im).ieta()])){
	ntowersWithJets_[(*im).ieta()]++;
	excludedTowers.push_back(std::pair<int,int>(im->ieta(),im->iphi()));
	if(nref < nMaxJets_) jtexngeom[nref]++;
      }
    }

    std::vector<fastjet::PseudoJet>::const_iterator it = fjInputs_.begin(),
      fjInputsEnd = fjInputs_.end();

    for(; it != fjInputsEnd; ++it){
      int index = it->user_index();
      int ie = ieta(inputs_[index]);
      int ip = iphi(inputs_[index]);
      std::vector<std::pair<int,int> >::const_iterator exclude = find(excludedTowers.begin(),excludedTowers.end(),std::pair<int,int>(ie,ip));
      if(exclude != excludedTowers.end()){
        jettowers.push_back(index);
      }
    }

    for(it = fjInputs_.begin(); it != fjInputsEnd; ++it){
      int index = it->user_index();
      const reco::CandidatePtr& originalTower = inputs_[index];
      double dr = reco::deltaR((*it),(*pseudojetTMP));

      if(dr < radiusPU_){
        if(nref < nMaxJets_){
          jtexntow[nref]++;
          jtexpt[nref] += originalTower->pt();
        }
      }      
    }



    if(nref < nMaxJets_) nref++;
  } // pseudojets    
  // Create a new collections from the towers not included in jets                                                  
  //                                                                                                                

  for(std::vector<fastjet::PseudoJet>::const_iterator it = fjInputs_.begin(),
        fjInputsEnd = fjInputs_.end(); it != fjInputsEnd; ++it){
    int index = it->user_index();
    std::vector<int>::const_iterator itjet = find(jettowers.begin(),jettowers.end(),index);
    if(itjet == jettowers.end()){
      const reco::CandidatePtr& originalTower = inputs_[index];
      fastjet::PseudoJet orphan(originalTower->px(),originalTower->py(),originalTower->pz(),originalTower->energy());
      orphan.set_user_index(index);
      orphanInput.push_back(orphan);
    }
  }
}


void HiPuRhoProducer::packageRho()
{
  unsigned int etaPos = 0;
  while(etaPos < etaEdgeLow_.size()){
    bool isSwapDone = false;
    for(unsigned int etaIter = etaPos+1; etaIter < etaEdgeLow_.size(); ++etaIter){
      if(etaEdgeLow_.at(etaPos) > etaEdgeLow_.at(etaIter)){
	double tempEtaEdgeLow = etaEdgeLow_.at(etaPos);
	double tempEtaEdgeHi = etaEdgeHi_.at(etaPos);
	double tempRho = rho_.at(etaPos);
	double tempRhoM = rhoM_.at(etaPos);

	etaEdgeLow_.at(etaPos) = etaEdgeLow_.at(etaIter);
	etaEdgeHi_.at(etaPos) = etaEdgeHi_.at(etaIter);
	rho_.at(etaPos) = rho_.at(etaIter);
	rhoM_.at(etaPos) = rhoM_.at(etaIter);

	etaEdgeLow_.at(etaIter) = tempEtaEdgeLow;
        etaEdgeHi_.at(etaIter) = tempEtaEdgeHi;
        rho_.at(etaIter) = tempRho;
        rhoM_.at(etaIter) = tempRhoM;

	isSwapDone = true;
      }
    }

    if(!isSwapDone) ++etaPos;
  }

  for(unsigned int etaIter = 0; etaIter < etaEdgeLow_.size(); ++etaIter){
    etaEdges_.push_back(etaEdgeLow_.at(etaIter));
  }
  etaEdges_.push_back(etaEdgeHi_.at(etaEdgeHi_.size()-1));
}


void HiPuRhoProducer::putRho(edm::Event& iEvent,const edm::EventSetup& iSetup)
{
  bool debug = false;
  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  std::auto_ptr<std::vector<double>> mapEtaRangesOut(new std::vector<double>(83,-999.));
  std::auto_ptr<std::vector<double>> mapToRhoOut(new std::vector<double>(82,-999.));
  std::auto_ptr<std::vector<double>> mapToRhoMOut(new std::vector<double>(82,-999.));

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  for(unsigned int etaIter = 0; etaIter < etaEdges_.size(); ++etaIter){
    mapEtaRangesOut->at(etaIter) = etaEdges_.at(etaIter);
  }

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  for(unsigned int rhoIter = 0; rhoIter < rho_.size(); ++rhoIter){
    mapToRhoOut->at(rhoIter) = rho_.at(rhoIter);
    mapToRhoMOut->at(rhoIter) = rhoM_.at(rhoIter);
  }

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;

  iEvent.put(mapEtaRangesOut, "mapEtaEdges");
  iEvent.put(mapToRhoOut, "mapToRho");
  iEvent.put(mapToRhoMOut, "mapToRhoM");

  if(debug) std::cout << __FILE__ << ", " << __LINE__ << std::endl;
}


// ------------ method called once each job just before starting event loop  ------------
void 
HiPuRhoProducer::beginJob()
{

}

// ------------ method called once each job just after ending the event loop  ------------
void 
HiPuRhoProducer::endJob() {
}
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void HiPuRhoProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


int HiPuRhoProducer::ieta(const reco::CandidatePtr & in) const {
  int it = 0;
  const CaloTower* ctc = dynamic_cast<const CaloTower*>(in.get());
  if(ctc){
    it = ctc->id().ieta();
  } else
    {
      throw cms::Exception("Invalid Constituent") << "CaloJet constituent is not of CaloTower type";
    }
  return it;
}

int HiPuRhoProducer::iphi(const reco::CandidatePtr & in) const {
  int it = 0;
  const CaloTower* ctc = dynamic_cast<const CaloTower*>(in.get());
  if(ctc){
    it = ctc->id().iphi();
  } else
    {
      throw cms::Exception("Invalid Constituent") << "CaloJet constituent is not of CaloTower type";
    }
  return it;
}



//define this as a plug-in
DEFINE_FWK_MODULE(HiPuRhoProducer);
