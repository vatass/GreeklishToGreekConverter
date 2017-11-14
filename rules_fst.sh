#!/bin/sh

name=$1
alph_en=$2
alph_el=$3

#rm  -rf fst_lang
#mkdir fst_lang

fstcompile --isymbols=$2 --osymbols=$3 ${name}.txt fst_lang/${name}.fst
fstdraw --portrait --isymbols=$2 --osymbols=$3 fst_lang/${name}.fst fst_lang/dot 
dot -Tjpg fst_lang/dot > alphabet_dict/${name}.jpg