#!/bin/sh

## $1 = alfavhto
## $2 = fakelos
## $3 = fst_I
## $4 = fst_E
## $5 = fst_S1

#creation of I
fstcompile --isymbols=$1 --osymbols=$1 $2/$3.txt $2/$3.fst

#creation of I*
fstclosure $2/$3.fst $2/$3_closure.fst

#creation of E (consists of I + what we gave it from txt)
fstcompile --isymbols=$1 --osymbols=$1 $2/$4.txt $2/temp1.fst
fstunion $2/$3.fst $2/temp1.fst $2/$4.fst

#creation of I* concat E
fstconcat $2/$3_closure.fst $2/$4.fst $2/temp.fst

#creation of  S1   =   (I* concat E) concat I*
fstconcat $2/temp.fst $2/$3_closure.fst $2/$5.fst
fstarcsort --sort_type=ilabel $2/$5.fst $2/$5.fst

#############################
#creation of  S2   =   (S1 concat E) concat I*
fstconcat $2/$5.fst $2/temp.fst $2/tempidi.fst
fstconcat $2/tempidi.fst $2/$3_closure.fst $2/$6.fst

fstarcsort --sort_type=ilabel $2/$6.fst $2/$6.fst

fstcompile --acceptor --isymbols=alphabet_dict/alphabet_el.syms lexicon_el.txt fsa_el/lexicon_el_new.fsa
fstdeterminize	fsa_el/lexicon_el_new.fsa fsa_el/lexicon_el_new_determ.fsa
fstminimize	fsa_el/lexicon_el_new_determ.fsa fsa_el/lexicon_el_new_minim.fsa

fstarcsort --sort_type=ilabel fsa_el/lexicon_el_new_minim.fsa fsa_el/lexicon_el_sorted.fst