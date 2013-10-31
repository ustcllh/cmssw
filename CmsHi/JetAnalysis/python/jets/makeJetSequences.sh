#!/bin/sh

echo "import FWCore.ParameterSet.Config as cms" > HiGenJetsCleaned_cff.py
echo "from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *" >> HiGenJetsCleaned_cff.py

for system in PbPb pp pPb
  do
  for sample in mc data
    do
    for algo in ak
      do
      for sub in Vs Pu NONE
	do
	for radius in 2 3 4 5 6 7
	  do
	  matchobject="Calo"
	  for object in PF Calo
	    do

	    subt=$sub
	    if [ $sub == "NONE" ]; then
		subt=""
	    fi
	    
	    ismc="False"
	    corrlabel="_hiIterativeTracks"
            domatch="True"
            genjets="HiGenJetsCleaned"
	    genparticles="hiGenParticles"
            tracks="hiGeneralTracks"
            pflow="particleFlowTmp"
            match=${algo}${subt}${radius}${matchobject}
            echo "" > $algo$subt$radius${object}JetSequence_${system}_${sample}_cff.py

            if [ $system != "PbPb" ]; then
		corrlabel="_generalTracks"
		tracks="generalTracks"
		genparticles="genParticles"
            fi

	    if [ $object == "Calo" ]; then
		corrlabel="_HI"
		domatch="False"
	    fi

	    if [ $sample == "mc" ]; then
		ismc="True"
	    fi

	    if [ $system == "pp" ]; then
		genjets="HiGenJets"
	    fi

            corrname=`echo ${algo} | sed 's/\(.*\)/\U\1/'`${radius}${object}${corrlabel}

	    if [ $system == "PbPb" ] && [ $sample == "mc" ] && [ $object == "PF" ] && [ $sub == "Vs" ]; then
		
		cat templateClean_cff.py.txt \
		    | sed "s/ALGO_/$algo/g" \
		    | sed "s/SUB_/$subt/g" \
		    | sed "s/RADIUS_/$radius/g" \
		    | sed "s/OBJECT_/$object/g" \
		    | sed "s/SAMPLE_/$sample/g" \
		    | sed "s/CORRNAME_/$corrname/g" \
		    | sed "s/MATCHED_/$match/g" \
		    | sed "s/ISMC/$ismc/g" \
		    | sed "s/GENJETS/$genjets/g" \
		    | sed "s/GENPARTICLES/$genparticles/g" \
		    | sed "s/TRACKS/$tracks/g" \
		    | sed "s/PARTICLEFLOW/$pflow/g" \
		    | sed "s/DOMATCH/$domatch/g" \
		    >> HiGenJetsCleaned_cff.py
	    fi
	    
	    cat templateSequence_cff.py.txt \
		| sed "s/ALGO_/$algo/g" \
		| sed "s/SUB_/$subt/g" \
		| sed "s/RADIUS_/$radius/g" \
		| sed "s/OBJECT_/$object/g" \
		| sed "s/SAMPLE_/$sample/g" \
		| sed "s/CORRNAME_/$corrname/g" \
		| sed "s/MATCHED_/$match/g" \
		| sed "s/ISMC/$ismc/g" \
		| sed "s/GENJETS/$genjets/g" \
		| sed "s/GENPARTICLES/$genparticles/g" \
		| sed "s/TRACKS/$tracks/g" \
		| sed "s/PARTICLEFLOW/$pflow/g" \
		| sed "s/DOMATCH/$domatch/g" \
		>> $algo$subt$radius${object}JetSequence_${system}_${sample}_cff.py
	    
	  done
	done
      done
    done
  done
done

echo "" >> HiGenJetsCleaned_cff.py
echo "hiGenJetsCleaned = cms.Sequence(" >> HiGenJetsCleaned_cff.py

for algo in ak
  do
  for radius in 2 3 4 5 6 7
    do
    echo "$algo${radius}HiGenJetsCleaned" >> HiGenJetsCleaned_cff.py
    if [ $radius -ne 7 ]; then
	echo "+" >> HiGenJetsCleaned_cff.py
    else
	echo ")" >> HiGenJetsCleaned_cff.py
    fi
    
  done
done
