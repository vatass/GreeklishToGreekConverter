def main():
    import shutil
    import subprocess
    import os

    filename_en = 'alphabet_dict/alphabet_en.syms'
    filename_el = 'alphabet_dict/alphabet_el.syms'
    lex_creation('temp/t1.txt', filename_en, 1)
    lex_creation('temp/t2.txt', filename_el, 0)

    #shutil.rmtree('prob')
    #shutil.rmtree('temp')

    if os.path.isdir('fst_lang'):
        shutil.rmtree('fst_lang')
    os.mkdir('fst_lang')

    probs = open('probs.txt', 'r')
    filename_probs = 'probs_fst'
    probs_fst = open(filename_probs+'.txt', 'w')
    for line in probs:
        curr_state = str(0) + ' ' + str(1) + ' ' + line
        probs_fst.write(curr_state)
    probs_fst.write(str(1)+'\n')
    probs_fst.close()

    bash_call = 'bash rules_fst.sh ' + filename_probs + ' ' + filename_en + ' ' + filename_el
    subprocess.call(bash_call, shell=True)



    filename_alph = 'alph_fst'

    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    alph_fst = open(filename_alph+'.txt', 'w')
    alph_name = 'temp/t3.txt'
    alph_lex = open(alph_name, 'w')
    for curr in alphabet:
        alph_lex.write(curr+'\n')

        p = 1000.0
        curr_state = str(0) + ' ' + str(1) + ' ' + curr + ' ' + curr + ' '+str(p) + '\n'
        alph_fst.write(curr_state)

    alph_fst.write(str(1)+'\n')
    alph_fst.close()
    alph_lex.close()

    telos = 'alphabet_dict/extra_alphabet'
    lex_creation(alph_name, telos, 0)

    bash_call = 'bash rules_fst.sh ' + filename_alph + ' ' + telos + ' ' + telos
    subprocess.call(bash_call, shell=True)

    

def lex_creation(temp, filename,flag):
    t = open(temp, 'r')
    lines = t.readlines()
    t.close()

    shit = map(lambda s: s.strip(), lines)  # to remove \n from all the elements
    shit = sorted(list(set(shit)))  # sort elements

    alph = open(filename, 'w')
    alph.write('<epsilon> 0\n')
    counter = 1
    for line in shit:
        alph.write(str(line) + ' ' + str(counter) + '\n')
        counter = counter + 1

    if flag==1: # only in english alphabet creation
        alph.write('Q '+str(counter)+'\n')

    alph.close()


main()