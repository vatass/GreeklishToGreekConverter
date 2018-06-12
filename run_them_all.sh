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
python greeklish_conversion_test.py

## bhma 12 i) ii) iii)
echo 'Finding faults between correct and wrong train texts...'
python newspeller.py

echo ' '
echo 'Please run newspeller.py script now'
echo 'Then run script run_them_all2.sh'

