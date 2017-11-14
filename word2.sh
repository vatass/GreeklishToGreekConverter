#!/bin/sh


fstcompile --acceptor --isymbols=alphabet_dict/alphabet_en.syms $2/$1.txt $2/$1.fsa

fstarcsort --sort_type=olabel $2/$1.fsa $2/$1_sorted.fst

fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_en.syms $2/$1_sorted.fst $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_00.jpg
fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_en.syms $2/$1_sorted.fst $2/$1_sorted.txt

# converter already sorted
fstcompose  $2/$1_sorted.fst fst_greeklish/greeklish_converter_sorted.fst  $2/$1_to_greek.fst
#fstcompose  $2/$1.fsa fst_greeklish/greeklish_converter_sorted.fst  $2/$1_to_greek.fst

fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek.fst $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_0.jpg
fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_en.syms $2/$1_to_greek.fst $2/$1_to_greek.txt

fstrmepsilon $2/$1_to_greek.fst $2/$1_to_greek_rmeps.fst

fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_rmeps.fst $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_1.jpg
fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_rmeps.fst $2/$1_to_greek_rmeps.txt

fstshortestpath --unique $2/$1_to_greek_rmeps.fst $2/$1_to_greek_shortest.fst

fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_shortest.fst $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_2.jpg
fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_shortest.fst $2/$1_to_greek_shortest.txt