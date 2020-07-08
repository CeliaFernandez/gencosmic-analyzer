#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

#include "DataFormats/Common/interface/Handle.h"
/*
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/Common/interface/RefToBase.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PFIsolation.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/MET.h"
*/

/*
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/AdaptiveVertexFit/interface/AdaptiveVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/VertexTools/interface/GeometricAnnealing.h"

#include "RecoBTag/SecondaryVertex/interface/SecondaryVertex.h"
#include "RecoBTag/SecondaryVertex/interface/TrackKinematics.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
*/

#include "DataFormats/Candidate/interface/Candidate.h"


#include "DataFormats/HepMCCandidate/interface/GenParticle.h"


//#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
//#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"



//#include "DataFormats/MuonReco/interface/MuonFwd.h" 

#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

#include "TLorentzVector.h"
#include "TTree.h"
#include "TFile.h"


//=======================================================================================================================================================================================================================//


///////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////// FUNCTIONS ///////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////// DATA DEFINITION //////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////



class gencosmicproducer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit gencosmicproducer(const edm::ParameterSet&);
      ~gencosmicproducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      edm::ParameterSet parameters;
      std::string output_filename;

      //// Get Tokens ////
      edm::EDGetTokenT<edm::View<reco::GenParticle> > theGenParticleCollection;

      //// General info /////
      Int_t Event_event;
      Int_t Event_run;
      Int_t Event_luminosityBlock;

      Int_t nM; // Number muons
      Float_t Muon_pt[100];
      Float_t Muon_eta[100];
      Float_t Muon_phi[100];
      Float_t Muon_status[100];
      Float_t Muon_vx[100];
      Float_t Muon_vy[100];



      // Output definition:
      TFile *file_out;
      TTree *tree_out;

};
//=======================================================================================================================================================================================================================//




//=======================================================================================================================================================================================================================//
gencosmicproducer::gencosmicproducer(const edm::ParameterSet& iConfig)
{
   usesResource("TFileService");
   
   parameters = iConfig;

   theGenParticleCollection = consumes<edm::View<reco::GenParticle> >  (parameters.getParameter<edm::InputTag>("GenParticleCollection"));

}
//=======================================================================================================================================================================================================================//




//=======================================================================================================================================================================================================================//
gencosmicproducer::~gencosmicproducer()
{

}
//=======================================================================================================================================================================================================================//



//=======================================================================================================================================================================================================================//
void gencosmicproducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   /////////////////////////////////////////////////////////////////////////////////////
   ///////////////////////////////////// MAIN CODE /////////////////////////////////////
   /////////////////////////////////////////////////////////////////////////////////////



   //////////////////////////////// GET THE COLLECTIONS ////////////////////////////////
   
   // genParticles collection
   edm::Handle<edm::View<reco::GenParticle> > genParticles;
   iEvent.getByToken(theGenParticleCollection, genParticles);

  
   //////////////////////////////// EVENT INFO  ////////////////////////////////
   Event_event = iEvent.id().event();
   Event_run = iEvent.id().run();
   Event_luminosityBlock = iEvent.id().luminosityBlock();

   std::cout << "Event number " << Event_event << std::endl;

   //////////////////////////////// GENERATED PARTICLES  ////////////////////////////////

   nM = 0; // Number muons
   int iM = -99; // Index of the status = 1 cosmic muon

   // Loop to identify the generated muons
   for(size_t i = 0; i < genParticles->size(); i++) {

      const reco::GenParticle &particle = (*genParticles)[i];

      if ( abs( particle.pdgId() ) == 13 ){

         if ( particle.status() == 1 ) { iM = i; }

         Muon_pt[nM] = particle.pt();
         Muon_eta[nM] = particle.eta();
         Muon_phi[nM] = particle.phi();
         Muon_status[nM] = particle.status();
         Muon_vx[nM] = particle.vx();
         Muon_vy[nM] = particle.vy();
     
         /* 
         std::cout << "Gen muon: " << nM << std::endl;
         std::cout << "Status: " << particle.status() << std::endl;
         std::cout << "isFirstCopy: " << particle.isFirstCopy() << std::endl;
         std::cout << "isLastCopy: " << particle.isLastCopy() << std::endl;
         std::cout << "Pt: " << particle.pt() << std::endl;
         std::cout << "Phi: " << particle.phi() << std::endl;
         std::cout << "Eta: " << particle.eta() << std::endl;
         */

         nM++;
      }

   }


   // Navigation over the status = 1 muon
   const reco::GenParticle &muon1 = (*genParticles)[iM];
   reco::GenParticleRef mref;
   reco::GenParticle m;


   std::cout << "Status: 1" << std::endl;
   std::cout << "pt, eta, phi: " << muon1.pt() << ", " << muon1.eta() << ", " << muon1.phi() << std::endl;
   std::cout << "vx, vy: " << muon1.vx() << ", " << muon1.vy() << std::endl;

   if (muon1.mother()->pdgId() == muon1.pdgId()) {

      mref = muon1.motherRef(); m = *mref;
      std::cout << "Status: " << m.status() << std::endl;
      std::cout << "pt, eta, phi: " << m.pt() << ", " << m.eta() << ", " << m.phi() << std::endl;
      std::cout << "vx, vy: " << m.vx() << ", " << m.vy() << std::endl;

      while (m.pdgId() == m.mother()->pdgId()) {

         mref = m.motherRef();
         m = *mref;

         std::cout << "Status: " << m.status() << std::endl;
         std::cout << "pt, eta, phi: " << m.pt() << ", " << m.eta() << ", " << m.phi() << std::endl;
         std::cout << "vx, vy: " << m.vx() << ", " << m.vy() << std::endl;

         if (m.numberOfMothers() == 0) {break;}

      }

   }


   // Fill the tree
   tree_out->Fill();

}











//=======================================================================================================================================================================================================================//




//=======================================================================================================================================================================================================================//
void gencosmicproducer::beginJob()
{
  std::cout << "Begin Job" << std::endl;

  output_filename = parameters.getParameter<std::string>("nameOfOutput");
  file_out = new TFile(output_filename.c_str(), "RECREATE");


  // -> Output tree definition

  tree_out = new TTree("Events", "Events"); // declaration

  // Branches:

  tree_out->Branch("Event_event", &Event_event, "Event_event/I");

  tree_out->Branch("nM", &nM, "nM/I");
  tree_out->Branch("Muon_pt", Muon_pt, "Muon_pt[nM]/F");
  tree_out->Branch("Muon_eta", Muon_eta, "Muon_eta[nM]/F");
  tree_out->Branch("Muon_phi", Muon_phi, "Muon_phi[nM]/F");
  tree_out->Branch("Muon_status", Muon_status, "Muon_status[nM]/F");

}
//=======================================================================================================================================================================================================================//
void gencosmicproducer::endJob()
{
  std::cout << "End Job" << std::endl;

  file_out->cd();
  tree_out->Write();
  file_out->Close();

}




//=======================================================================================================================================================================================================================//
void gencosmicproducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//=======================================================================================================================================================================================================================//
/*
void gencosmicproducer::getCorrectDaughter(const reco::Candidate *c)
{

   for (size_t q = 0; q < c->numberOfDaughters(); q++){

      if (c->pdgId() == c->daughter(q)->pdgId()) { return q; }

   }

   return -1;

}
*/


DEFINE_FWK_MODULE(gencosmicproducer);
