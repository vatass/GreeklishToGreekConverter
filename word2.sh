#!/bin/sh


fstcompile --acceptor --isymbols=alphabet_dict/alphabet_mutual.syms $2/$1.txt $2/$1.fsa

fstdeterminize	$2/$1.fsa $2/$1_determ.fsa
fstminimize	$2/$1_determ.fsa $2/$1_minim.fsa


fstarcsort --sort_type=olabel $2/$1_minim.fsa $2/$1_sorted.fst

# converter already sorted
fstcompose  $2/$1_sorted.fst fst_greeklish/greeklish_converter_sorted.fst  $2/$1_to_greek.fst
fstrmepsilon $2/$1_to_greek.fst $2/$1_to_greek_rmeps.fst

fstshortestpath $2/$1_to_greek_rmeps.fst $2/$1_to_greek_shortest.fst
fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek_shortest.fst $2/$1_to_greek_shortest.txt
