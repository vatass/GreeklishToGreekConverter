#!/usr/bin/env bash

rm -rf fst_greeklish
mkdir fst_greeklish

fstunion fsa_el/lexicon_el_minim.fsa fsa_en/lexicon_en_minim.fsa fst_greeklish/lexicon_total.fst

fstclosure fst_lang/probs_fst.fst fst_lang/probs_fst_closure.fst

# sort output labels of first transducer
fstarcsort --sort_type=ilabel fst_greeklish/lexicon_total.fst fst_greeklish/lexicon_total_sorted.fst
fstarcsort --sort_type=olabel fst_lang/probs_fst_closure.fst  fst_lang/probs_fst_closure_sorted.fst 

fstcompose fst_lang/probs_fst_closure_sorted.fst fst_greeklish/lexicon_total_sorted.fst fst_greeklish/greeklish_converter.fst

fstarcsort --sort_type=ilabel fst_greeklish/greeklish_converter.fst  fst_greeklish/greeklish_converter_sorted.fst
