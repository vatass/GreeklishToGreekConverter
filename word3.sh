#!/bin/sh

## $3 = type of converter (S1 or S2)
## $2 = fst_wrong
## $1 = filename of current acceptor

fstcompile --acceptor --isymbols=alphabet_dict/alphabet_el.syms $2/$1.txt $2/$1.fsa
fstarcsort --sort_type=olabel $2/$1.fsa $2/$1_sorted.fst


fstcompose $2/$1_sorted.fst fst_spellcheck/fst_$3.fst $2/$1_W_convS.fst  #find every possible transformation for each word
fstrmepsilon $2/$1_W_convS.fst $2/$1_W_convS_rmeps.fst

fstarcsort --sort_type=olabel $2/$1_W_convS_rmeps.fst $2/$1_W_convS_rmeps_sorted.fst

fstcompose $2/$1_W_convS_rmeps_sorted.fst fsa_el/lexicon_el_sorted.fst $2/$1_possible_sols.fst #find every possible transformation for each word
fstrmepsilon $2/$1_possible_sols.fst $2/$1_possible_sols_rmeps.fst

fstshortestpath $2/$1_possible_sols_rmeps.fst $2/$1_final.fst
fstprint --isymbols=alphabet_dict/alphabet_el.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_final.fst $2/$1_final_$3.txt

rm  -rf $2/*.fs*