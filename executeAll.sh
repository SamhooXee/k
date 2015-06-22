#!/bin/bash
date > start.txt
echo step -1 ----------------------------
rm -rf *.csv
echo step 0 -----------------------------
rm -rf usefulCurrent/*
echo remove usefulCurrent Done?
sleep 30
python parseALL.py
chmod +x gethistory.sh
./gethistory.sh
echo step 1 -----------------------------
sleep 120
python parse.py > mvNouse.sh 
echo step 1.1 - remove nouse file -------
rm -rf nouse/*
rm -rf useful/*
./mvNouse.sh
echo step 2 -----------------------------
python parse_step2.py > result.csv
date +%Y-%m-%d | xargs -I {} mv result.csv result/{}.csv
echo done !!!
date > stop.txt
