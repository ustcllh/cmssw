#ifndef HiJetBackground_HiFJRhoFlowModulationProducer_h
#define HiJetBackground_HiFJRhoFlowModulationProducer_h


// system include files
#include <memory>
#include <sstream>
#include <string>
#include <vector>

// user include files
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "TMath.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

class HiFJRhoFlowModulationProducer : public edm::EDProducer {
   public:
      explicit HiFJRhoFlowModulationProducer(const edm::ParameterSet&);
      ~HiFJRhoFlowModulationProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
  /// @name setting a new event
  //\{
  //----------------------------------------------------------------

  /// tell the background estimator that it has a new event, composed
  /// of the specified particles.


private:  
  ///input parameters
    
  /// input tokens
  edm::EDGetTokenT<edm::View<reco::Jet>>                 jetsToken_;
  edm::EDGetTokenT<reco::PFCandidateCollection>          pfCandsToken_;
  edm::EDGetTokenT<std::vector<double>>                  mapEtaToken_;
  edm::EDGetTokenT<std::vector<double>>                  mapRhoToken_;
  edm::EDGetTokenT<std::vector<double>>                  mapRhoMToken_;
  
};

#endif

