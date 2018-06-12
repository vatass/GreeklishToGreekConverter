def main():
    import shutil
    import subprocess
    import os

    filename_en = 'alphabet_dict/alphabet_en.syms'
    filename_el = 'alphabet_dict/alphabet_el.syms'
    lex_creation('temp/t1.txt', filename_en, 1)
    lex_creation('temp/t2.txt', filename_el, 0)


    ###################################
    # create mutual alphabet

    filename_mut = 'alphabet_dict/alphabet_mutual.syms'
    tot = open(filename_mut, 'w')

    curr_file = open('alphabet_dict/alphabet_en.syms', 'r')
    cnt_lines = 0
    for line in curr_file:
        tot.write(line)
        cnt_lines = cnt_lines + 1
    curr_file.close()
    new_cnt = cnt_lines
    curr_file = open('alphabet_dict/alphabet_el.syms', 'r')
    for line in curr_file:
        new_cnt = new_cnt + 1
        if new_cnt == cnt_lines + 1:
            continue
        s = line.split()
        new_line = s[0] + ' ' + str(new_cnt - 2) + '\n'
        tot.write(new_line)
    curr_file.close()
    tot.close()
    ###################################

    # shutil.rmtree('prob')
    # shutil.rmtree('temp')

    if os.path.isdir('fst_lang'):
        shutil.rmtree('fst_lang')
    os.mkdir('fst_lang')

    probs = open('probs.txt', 'r')
    filename_probs = 'probs_fst'
    probs_fst = open(filename_probs + '.txt', 'w')
    for line in probs:
        curr_state = str(0) + ' ' + str(1) + ' ' + line
        probs_fst.write(curr_state)
    probs_fst.write(str(1) + '\n')
    probs_fst.close()

    #bash_call = 'bash rules_fst.sh ' + filename_probs + ' ' + filename_en + ' ' + filename_el
    bash_call = 'bash rules_fst.sh ' + filename_probs + ' ' + filename_mut + ' ' + filename_mut

    subprocess.call(bash_call, shell=True)


    filename_alph = 'alph_fst'
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    alph_fst = open(filename_alph + '.txt', 'w')
    alph_name = 'temp/t3.txt'
    alph_lex = open(alph_name, 'w')
    for curr in alphabet:
        alph_lex.write(curr + '\n')

        p = 1000.0
        curr_state = str(0) + ' ' + str(1) + ' ' + curr + ' ' + curr + ' ' + str(p) + '\n'
        alph_fst.write(curr_state)

    alph_fst.write(str(1) + '\n')
    alph_fst.close()
    alph_lex.close()

    telos = 'alphabet_dict/extra_alphabet.syms'
    lex_creation(alph_name, telos, 0)

    #bash_call = 'bash rules_fst.sh ' + filename_alph + ' ' + telos + ' ' + telos
    bash_call = 'bash rules_fst.sh ' + filename_alph + ' ' + filename_mut + ' ' + filename_mut
    subprocess.call(bash_call, shell=True)





def lex_creation(temp, filename, flag):
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

    if flag == 1:  # only in english alphabet creation
        alph.write('Q ' + str(counter) + '\n')

    alph.close()


main()
