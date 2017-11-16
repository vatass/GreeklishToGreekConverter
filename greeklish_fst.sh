#!/usr/bin/env bash

rm -rf fst_greeklish
mkdir fst_greeklish


fstunion fsa_el/lexicon_el_minim.fsa fsa_en/lexicon_en_minim.fsa fst_greeklish/lexicon_total.fst
#fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fst_greeklish/lexicon_total.fsa fst_greeklish/lexicon_total_fsa.txt



#fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fst_greeklish/lexicon_total.fst fst_greeklish/lexicon_total.txt
#fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fsa_el/lexicon_el_minim.fsa    fst_greeklish/lexicon_el_minim.txt
#fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fsa_en/lexicon_en_minim.fsa    fst_greeklish/lexicon_en_minim.txt
#fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fsa_el/lexicon_el.fsa          fst_greeklish/lexicon_el.txt
#fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fsa_en/lexicon_en.fsa          fst_greeklish/lexicon_en.txt



#fstunion fst_lang/probs_fst.fst fst_lang/alph_fst.fst fst_lang/probs_fst_new.fst
#fstclosure fst_lang/probs_fst_new.fst fst_lang/probs_fst_closure.fst

fstunion fst_lang/probs_fst.fst fst_lang/alph_fst.fst fst_lang/probs_fst_new1.fst
fstrmepsilon fst_lang/probs_fst_new1.fst fst_lang/probs_fst_new.fst

fstclosure fst_lang/probs_fst_new.fst fst_lang/probs_fst_closure1.fst
fstrmepsilon fst_lang/probs_fst_closure1.fst fst_lang/probs_fst_closure.fst


fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fst_lang/probs_fst_closure.fst fst_lang/probs_fst_closure.txt
fstprint --isymbols=alphabet_dict/alphabet_mutual.syms --osymbols=alphabet_dict/alphabet_mutual.syms fst_lang/probs_fst_new.fst fst_lang/probs_fst_new.txt



# sort output labels of first transducer
fstarcsort --sort_type=ilabel fst_greeklish/lexicon_total.fst fst_greeklish/lexicon_total_sorted.fst
fstarcsort --sort_type=olabel fst_lang/probs_fst_closure.fst  fst_lang/probs_fst_closure_sorted.fst
fstcompose fst_lang/probs_fst_closure_sorted.fst fst_greeklish/lexicon_total_sorted.fst fst_greeklish/greeklish_converter.fst
fstarcsort --sort_type=ilabel fst_greeklish/greeklish_converter.fst  fst_greeklish/greeklish_converter_sorted.fst

###
#fstrmepsilon fst_greeklish/greeklish_converter.fst fst_greeklish/greeklish_converter_rm.fst
#fstarcsort --sort_type=ilabel fst_greeklish/greeklish_converter_rm.fst  fst_greeklish/greeklish_converter_sorted.fst
###



