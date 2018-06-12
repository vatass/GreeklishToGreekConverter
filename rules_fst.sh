#!/bin/sh

name=$1
alph_en=$2
alph_el=$3


fstcompile --isymbols=$2 --osymbols=$3 ${name}.txt fst_lang/${name}.fst