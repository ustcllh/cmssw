// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"


#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Common/interface/TriggerResultsByName.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TNtuple.h"

using namespace std;
using namespace edm;

//
// class declaration
//

class TriggerObjectAnalyzer : public edm::EDAnalyzer {
   public:
      explicit TriggerObjectAnalyzer(const edm::ParameterSet&);
      ~TriggerObjectAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

  std::string   processName_;
  std::vector<std::string>   triggerNames_;
  edm::InputTag triggerResultsTag_;
  edm::InputTag triggerEventTag_;

  edm::Handle<edm::TriggerResults>   triggerResultsHandle_;
  edm::Handle<trigger::TriggerEvent> triggerEventHandle_;

  HLTConfigProvider hltConfig_;

  unsigned int triggerIndex_;
  unsigned int moduleIndex_;
  string moduleLabel_;
  vector<string> moduleLabels_;

  edm::Service<TFileService> fs;
  vector<TNtuple*> nt_;
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
TriggerObjectAnalyzer::TriggerObjectAnalyzer(const edm::ParameterSet& ps):
  processName_(ps.getParameter<std::string>("processName")),
  triggerNames_(ps.getParameter<std::vector<std::string> >("triggerNames")),
  triggerResultsTag_(ps.getParameter<edm::InputTag>("triggerResults")),
  triggerEventTag_(ps.getParameter<edm::InputTag>("triggerEvent"))
{
   //now do what ever initialization is needed
  nt_.reserve(triggerNames_.size());
  nt_[0] = fs->make<TNtuple>(triggerNames_[0].data(),triggerNames_[0].data(),"id:pt:eta:phi:mass");

}


TriggerObjectAnalyzer::~TriggerObjectAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TriggerObjectAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  float id = -99,pt=-99,eta=-99,phi=-99,mass=-99;

   using namespace edm;
   iEvent.getByLabel(triggerEventTag_,triggerEventHandle_);
   iEvent.getByLabel(triggerResultsTag_,triggerResultsHandle_);

   moduleIndex_ = triggerResultsHandle_->index(triggerIndex_);

   // Results from TriggerEvent product - Attention: must look only for
   // modules actually run in this path for this event!
   for (unsigned int j=0; j<=moduleIndex_; ++j) {
     // check whether the module is packed up in TriggerEvent product
     const string& moduleLabel(moduleLabels_[j]);
     const string  moduleType(hltConfig_.moduleType(moduleLabel));
     const unsigned int filterIndex(triggerEventHandle_->filterIndex(InputTag(moduleLabel_,"",processName_)));
     if (filterIndex<triggerEventHandle_->sizeFilters()) {
       const trigger::Vids& VIDS (triggerEventHandle_->filterIds(filterIndex));
       const trigger::Keys& KEYS(triggerEventHandle_->filterKeys(filterIndex));
       const unsigned int nI(VIDS.size());
       const unsigned int nK(KEYS.size());
       assert(nI==nK);
       const unsigned int n(max(nI,nK));

       const trigger::TriggerObjectCollection& TOC(triggerEventHandle_->getObjects());
       for (unsigned int i=0; n != 0 && i < 1; ++i) {
	 const trigger::TriggerObject& TO(TOC[KEYS[i]]);
	 
	 id = TO.id();
	 pt = TO.pt();
	 eta = TO.eta();
	 phi = TO.phi();
	 mass = TO.mass();
       }
     }
   }

   nt_[0]->Fill(id,pt,eta,phi,mass);

}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerObjectAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerObjectAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
TriggerObjectAnalyzer::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
{
  bool changed(true);
  if (hltConfig_.init(iRun,iSetup,processName_,changed)) {
    if (changed) {
      if (triggerNames_[0]!="@") { // "@" means: analyze all triggers in config
	const unsigned int n(hltConfig_.size());
	triggerIndex_ = hltConfig_.triggerIndex(triggerNames_[0]);
	moduleLabels_ = hltConfig_.moduleLabels(triggerIndex_);

	if (triggerIndex_>=n) {
	  cout << "HLTEventAnalyzerAOD::analyze:"
	       << " TriggerName " << triggerNames_[0] 
	       << " not available in (new) config!" << endl;
	  cout << "Available TriggerNames are: " << endl;
	  hltConfig_.dump("Triggers");
	}
      }
      hltConfig_.dump("ProcessName");
      hltConfig_.dump("GlobalTag");
      hltConfig_.dump("TableName");
      hltConfig_.dump("Streams");
      hltConfig_.dump("Datasets");
      hltConfig_.dump("PrescaleTable");
      hltConfig_.dump("ProcessPSet");
    }
  } else {
    cout << "HLTEventAnalyzerAOD::analyze:"
	 << " config extraction failure with process name "
	 << processName_ << endl;
  }

}

// ------------ method called when ending the processing of a run  ------------
void 
TriggerObjectAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TriggerObjectAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TriggerObjectAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerObjectAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerObjectAnalyzer);
