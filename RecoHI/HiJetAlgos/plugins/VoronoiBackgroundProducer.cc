// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/HeavyIonEvent/interface/VoronoiBackground.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"

#include "RecoHI/HiJetAlgos/interface/VoronoiAlgorithm.h"

using namespace std;
//
// class declaration
//

class VoronoiBackgroundProducer : public edm::EDProducer {
   public:
      explicit VoronoiBackgroundProducer(const edm::ParameterSet&);
      ~VoronoiBackgroundProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void produce(edm::Event&, const edm::EventSetup&);
      
      // ----------member data ---------------------------

   edm::InputTag src_;
   VoronoiAlgorithm* voronoi_;
   bool doEqualize_;
   double equalizeThreshold0_;
   double equalizeThreshold1_;
   double equalizeR_;
   bool isCalo_;
   std::vector<reco::VoronoiBackground> vvm;

};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
VoronoiBackgroundProducer::VoronoiBackgroundProducer(const edm::ParameterSet& iConfig):
   voronoi_(0),
   doEqualize_(iConfig.getParameter<bool>("doEqualize")),
   equalizeThreshold0_(iConfig.getParameter<double>("equalizeThreshold0")),
   equalizeThreshold1_(iConfig.getParameter<double>("equalizeThreshold1")),
   equalizeR_(iConfig.getParameter<double>("equalizeR")),
   isCalo_(iConfig.getParameter<bool>("isCalo"))
{

   src_ = iConfig.getParameter<edm::InputTag>("src");
   //register your products

   produces<reco::VoronoiMap>();
   produces<std::vector<float> >();
}


VoronoiBackgroundProducer::~VoronoiBackgroundProducer()
{
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
VoronoiBackgroundProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   if(voronoi_ == 0){
     bool data = iEvent.isRealData();
     voronoi_ = new VoronoiAlgorithm(equalizeR_,data,isCalo_,std::pair<double, double>(equalizeThreshold0_,equalizeThreshold1_),doEqualize_);
   }

   voronoi_->clear();

   edm::Handle<reco::CandidateView> inputsHandle;
   iEvent.getByLabel(src_,inputsHandle);
   std::auto_ptr<reco::VoronoiMap> mapout(new reco::VoronoiMap());
   std::auto_ptr<std::vector<float> > vnout(new std::vector<float>(0));

   reco::VoronoiMap::Filler filler(*mapout);
   vvm.clear();

   for(unsigned int i = 0; i < inputsHandle->size(); ++i){
      reco::CandidateViewRef ref(inputsHandle,i);
      voronoi_->push_back_particle(ref->pt(),ref->eta(),ref->phi(),0);
   }

   std::vector<double> momentum_perp_subtracted = (*voronoi_);

   for(unsigned int i = 0; i < inputsHandle->size(); ++i){
      reco::CandidateViewRef ref(inputsHandle,i);
      double newpt = momentum_perp_subtracted[i];
      reco::VoronoiBackground bkg(0,0,newpt,0,0,0,0);
      LogDebug("VoronoiBackgroundProducer")<<"Subtraction --- oldpt : "<<ref->pt()<<" --- newpt : "<<newpt<<endl;
      vvm.push_back(bkg);
   }

   filler.insert(inputsHandle,vvm.begin(),vvm.end());
   filler.fill();
   iEvent.put(vnout);
   iEvent.put(mapout);
 
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
VoronoiBackgroundProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(VoronoiBackgroundProducer);
