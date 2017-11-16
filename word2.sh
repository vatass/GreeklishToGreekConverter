#!/bin/sh


#fstcompile --acceptor --isymbols=alphabet_dict/alphabet_en.syms $2/$1.txt $2/$1.fsa
fstcompile --acceptor --isymbols=alphabet_dict/alphabet_mutual.syms $2/$1.txt $2/$1.fsa
fstarcsort --sort_type=olabel $2/$1.fsa $2/$1_sorted.fst

# converter already sorted
fstcompose  $2/$1_sorted.fst fst_greeklish/greeklish_converter_sorted.fst  $2/$1_to_greek.fst

fstrmepsilon $2/$1_to_greek.fst $2/$1_to_greek_rmeps.fst

fstshortestpath $2/$1_to_greek_rmeps.fst $2/$1_to_greek_shortest.fst
fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek_shortest.fst $2/$1_to_greek_shortest.txt

############################################################################################################################################
#fstdraw --portrait --acceptor --isymbols=alphabet_dict/alphabet_en.syms $2/$1.fsa $2/dot
# dot -Tjpg $2/dot > $2/pics/out_$1_0.jpg
#fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_en.syms $2/$1_sorted.fst $2/dot
#dot -Tjpg $2/dot > $2/pics/out_$1_1.jpg
#fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_en.syms $2/$1_sorted.fst $2/$1_sorted.txt
#fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek.fst $2/dot
#dot -Tjpg $2/dot > $2/pics/out_$1_2.jpg
#fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek.fst $2/$1_to_greek.txt
#fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_rmeps.fst $2/dot
#dot -Tjpg $2/dot > $2/pics/out_$1_3.jpg
#fstprint --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_rmeps.fst $2/$1_to_greek_rmeps.txt
#fstdraw --portrait --isymbols=alphabet_dict/alphabet_en.syms --osymbols=alphabet_dict/alphabet_el.syms $2/$1_to_greek_shortest.fst $2/dot
# dot -Tjpg $2/dot > $2/pics/out_$1_4.jpg
############################################################################################################################################


fstdraw --portrait --acceptor --isymbols=alphabet_dict/alphabet_mutual.syms $2/$1.fsa $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_1.jpg

fstdraw --portrait --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek.fst $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_2.jpg
fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek.fst $2/$1_to_greek.txt

fstdraw --portrait --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek_rmeps.fst $2/dot
dot -Tjpg $2/dot > $2/pics/out_$1_3.jpg
fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek_rmeps.fst $2/$1_to_greek_rmeps.txt

fstdraw --portrait --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms $2/$1_to_greek_shortest.fst $2/dot

rm  -rf $2/*.fs*