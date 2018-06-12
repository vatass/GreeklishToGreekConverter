import subprocess
import shutil
import os

if os.path.isdir('fst_spellcheck'):
    shutil.rmtree('fst_spellcheck')
os.mkdir('fst_spellcheck')

alph_f = 'alphabet_dict/alphabet_el.syms'
f = open(alph_f,'r')

filename_I = 'fst_I'
fst_I = open('fst_spellcheck/fst_I.txt','w')

for line in f:
    if '<epsilon>' in line: #ignore first line
        continue
    s = line.split()
    if(len(s[0])==4): #ignore double characters (e.g. LL)
        continue
    curr_state = str(0) + ' ' + str(1) + ' ' + s[0] + ' ' + s[0] + ' ' + '0.0' + '\n'
    fst_I.write(curr_state)

curr_state = str(1) + '\n'
fst_I.write(curr_state)
f.close()
fst_I.close()

faults = open('spell_rules/faults_found_probs.txt','r')
filename_E = 'fst_E'
fst_E = open('fst_spellcheck/fst_E.txt','w')

eps = '<epsilon>'
cnt = 2
for line in faults:
    s = line.split()
    if s[0] == 'del':
        if s[1]=='keno':
            curr_state = str(0) + ' ' + str(1) + ' ' + eps + ' ' + s[2] + ' ' + str(s[3]) + '\n'
            fst_E.write(curr_state)
        else:
            s2 = s[2]
            s22 = [s2[i:i + 2] for i in range(0, len(s2), 2)]
            p1 = s22[1]
            curr_state = str(0) + ' ' + str(cnt) + ' ' + eps + ' ' + p1 + ' ' + str(s[3]) + '\n'
            fst_E.write(curr_state)

            p2 = s22[0]
            curr_state = str(cnt) + ' ' + str(1) + ' ' + s[1] + ' ' + p2 + ' ' + str(0.001) + '\n'
            fst_E.write(curr_state)
            cnt = cnt + 1
    elif s[0] == 'extra':
        if s[2]=='keno':
            curr_state = str(0) + ' ' + str(1) + ' ' + s[1] + ' ' + eps + ' ' + str(s[3]) + '\n'
            fst_E.write(curr_state)
        else:
            s1 = s[1]
            s11 = [s1[i:i + 2] for i in range(0, len(s1), 2)]
            p1 = s11[1]
            curr_state = str(0) + ' ' + str(cnt) + ' ' + p1 + ' ' + eps + ' ' + str(s[3]) + '\n'

            fst_E.write(curr_state)
            p2 = s11[0]
            curr_state = str(cnt) + ' ' + str(1) + ' ' + s[2] + ' ' + p2 + ' ' + str(0.001) + '\n'
            fst_E.write(curr_state)
            cnt = cnt + 1

    elif s[0] == 'subs':
        curr_state = str(0) + ' ' + str(1) + ' ' + s[1] + ' ' + s[2] + ' ' + str(s[3]) + '\n'
        fst_E.write(curr_state)
        curr_state = str(0) + ' ' + str(1) + ' ' + s[2] + ' ' + s[1] + ' ' + str(s[3]) + '\n'
        fst_E.write(curr_state)
    else:
        curr_state = str(0) + ' ' + str(cnt) + ' ' + s[1] + ' ' + s[2] + ' ' + str(s[3]) + '\n'
        fst_E.write(curr_state)

        curr_state = str(cnt-1) + ' ' + str(1) + ' ' + s[2] + ' ' + s[1] + ' ' + str(0.001) + '\n'
        fst_E.write(curr_state)
        cnt = cnt+1

curr_state = str(1) + '\n'
fst_E.write(curr_state)

faults.close()
fst_E.close()


# creation of I,E,S1,S2 (erwthmata iv me vii)
filename_S1 = 'fst_S1'
filename_S2 = 'fst_S2'
bash_call = 'bash spellcheck_fst.sh ' +  alph_f + ' ' + 'fst_spellcheck' + ' '  + filename_I + ' ' + filename_E +  ' ' + filename_S1 + ' ' + filename_S2
subprocess.call(bash_call, shell=True)