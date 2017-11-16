#!/bin/sh

name=$1

rm  -rf $2 
mkdir $2

#fstcompile --acceptor --isymbols=alphabet_dict/alphabet_$3.syms $1.txt $2/$1.fsa
fstcompile --acceptor --isymbols=alphabet_dict/alphabet_mutual.syms $1.txt $2/$1.fsa

fstdeterminize	$2/$1.fsa $2/$1_determ.fsa

fstminimize	$2/$1_determ.fsa $2/$1_minim.fsa
