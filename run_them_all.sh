#!/bin/sh

#bhma 1-2
echo 'Finding Greeklish-Greek rules and calculating probabilities...'
python parser.py

#bhma 3-4
echo 'Creating Greeklish-Greek and English-English FSTs...'
python alph_create.py

## bhma 5-6
echo 'Creating Greek lexicon FSA...'
python lex_el.py

## bhma 7
echo 'Creating English dictionary FSA...'
python lex_en.py

## bhma 8
echo 'Creating Greeklish to English/Greek converter...'
./greeklish_fst.sh

## bhma 9-10-11
echo 'Running accuracy test of Greeklish to Greek conversion...'
python lex_greng.py