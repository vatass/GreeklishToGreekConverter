#!/bin/sh


## bhma 12 iv) v) vi) vii)
echo 'Creating FSTs for spell checking (and new FSA for Greek Lexicon)...'
python spell_check_fst.py

## bhma 12 x)
echo 'Running accuracy test of Spell Checker...'
python spellcheck_test.py