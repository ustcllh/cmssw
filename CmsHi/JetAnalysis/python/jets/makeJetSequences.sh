#!/bin/sh

for sample in mc data
  do
  for algo in ak
    do
    for sub in Vs Pu
      do
      for radius in 2 3 4 5 6 7
	do
	for object in PF Calo
	  do
	  capalgo=`echo $algo | sed 's/\(.*\)/\U\1/'`
	  cat templateSequence_cff.py.txt \
	      | sed "s/ALGO_/$algo/g" \
	      | sed "s/SUB_/$sub/g" \
	      | sed "s/RADIUS_/$radius/g" \
	      | sed "s/OBJECT_/$object/g" \
	      | sed "s/SAMPLE_/$sample/g" \
	      | sed "s/CAPALGO_/$capalgo/g" \
	      > $algo$sub$radius${object}JetSequence_${sample}_cff.py	  	  
	done
      done
    done
  done
done





