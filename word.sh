#!/bin/sh

name=$1

rm  -rf $2 
mkdir $2

fstcompile --acceptor --isymbols=alphabet_dict/alphabet_$3.syms $1.txt $2/$1.fsa

fstdeterminize	$2/$1.fsa $2/$1_determ.fsa

fstminimize	$2/$1_determ.fsa $2/$1_minim.fsa


#fstdraw --portrait --acceptor --isymbols=alphabet_dict/alphabet.syms $2/$1.fsa $2/dot
#dot -Tjpg $2/dot > $2/$1.jpg

#fstdraw --acceptor --portrait --isymbols=alphabet_dict/alphabet.syms $2/$1_determ.fsa $2/dot
#dot -Tjpg $2/dot > $2/$1_determ.jpg

#fstdraw --acceptor --portrait --isymbols=alphabet_dict/alphabet.syms $2/$1_minim.fsa $2/dot
#dot -Tjpg $2/dot > $2/$1_minim.jpg