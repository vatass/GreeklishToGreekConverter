import shutil
import os
import subprocess
import itertools

f1 = open("msgs/test_greng.txt", "r")
f2 = open("msgs/test_gr.txt", "r")

if os.path.isdir('fsa_greng'):
    shutil.rmtree('fsa_greng')

cnt_words = 0  # counter of dictionary words
correct_conversions = 0
eng_conv_greek = 0
not_classified = 0
wrong_conversions = 0

########################################################
## acquire special characters from rules already created
rules12 = open('rules/1_2_rules.txt', 'r')
doubles = []
for line in rules12:
    doubles.append(line.split()[0])
rules12.close()

rules21 = open('rules/2_1_rules.txt', 'r')

halves = []
kuro2 = []

for line in rules21:
    halves.append(line.split()[0])
    siwo = line.split()[1]
    siwo = map(''.join, zip(*[iter(siwo)] * 2))

    siwo2 = []
    siwo3 = []
    rules11 = open('rules/1_1_rules.txt', 'r')
    for line2 in rules11:
        splita = line2.split()
        if siwo[0] in splita[1]:
            siwo2.append(splita)
        if siwo[1] in splita[1]:
            siwo3.append(splita)

    rules11.close()
    # keep rule with greatest possibility

    siwo2 = sorted(siwo2, key=lambda x: x[2], reverse=True)
    siwo3 = sorted(siwo3, key=lambda x: x[2], reverse=True)

    siwo2 = [item[0] for item in siwo2]
    siwo3 = [item[0] for item in siwo3]

    sivoitis0 = []
    for i in itertools.product(siwo2,siwo3):
        sivoitis0.append(i)
    kuro2.append(sivoitis0)
rules21.close()
########################################################

for line1, line2 in zip(f1, f2):
    s1 = line1.split()
    s2 = line2.split()
    os.mkdir('fsa_greng')
    os.mkdir('fsa_greng/pics')

    for curword1, curword2 in zip(s1, s2):  # 1-1
        if len(curword1) == 0:
            break
        filename = 'word' + str(cnt_words)
        new_file = open('fsa_greng/' + filename + '.txt', 'w')
        cnt_words = cnt_words + 1

        if '\n' in curword2:
            curword2 = curword2[-1]
        s = list(curword1)

        if len(s) == 1:
            curr_char = s[0]
            curr_state = str(0) + ' ' + str(1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
        else:
            counter = 2  # mutual starting point ( omit 0 )
            for i in range(0, len(s) - 1, 1):
                curr_char = s[i]
                old_counter = counter
                # ###### workaround for gk, gg, nt, mb, mp ######
                if any(ext in curr_char for ext in halves):
                    # ###### workaround for ALL gk, gg, nt, mb, mp ######
                    l = [halves.index(i) for i in halves if curr_char in i]  # take all occurences of it
                    #ii = numpy.where(halves2 == curr_char)[0]
                    indices = [i for i, x in enumerate(halves) if x == curr_char]
                    curr_prosth = [kuro2[i] for i in indices]
                    curr_prosth2 = []
                    for i in curr_prosth:
                        curr_prosth2 = curr_prosth2 + i
                    odhgos_stoxos = old_counter+len(curr_prosth2)+1 # so as to point to steady point
                    for st in curr_prosth2:
                        curr_state = str(old_counter) + ' ' + str(counter+1) + ' ' + st[0] + '\n'
                        new_file.write(curr_state)
                        counter = counter+1
                        curr_state = str(counter) + ' ' + str(odhgos_stoxos) + ' ' + st[1] + '\n'
                        new_file.write(curr_state)
                    counter = odhgos_stoxos-1 # cause next moment it will be +1 (so as to point to right state)
                    # ###### workaround for ALL gk, gg, nt, mb, mp ######
                # ###### workaround for gk, gg, nt, mb, mp ######
                curr_state = str(old_counter) + ' ' + str(counter + 1) + ' ' + curr_char + '\n'
                counter = counter + 1
                new_file.write(curr_state)
            curr_char = s[len(s) - 1]
            curr_state = str(counter) + ' ' + str(1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
        # ###### workaround for theta, psi, ksi ######
        if any(ext in curword1 for ext in doubles):
            ss = 2  # mutual starting point ( omit 0 )
            new_counter = counter + 2
            flag = 0
            for i in range(0, len(s) - 1, 1):
                if flag == 1:
                    flag = 0
                    continue
                else:
                    curr_char = s[i]

                    if i < (len(s) - 1):
                        curr_duo = s[i] + s[i + 1]
                    else:
                        curr_duo = s[i]
                    if any(ext in curr_duo for ext in doubles):
                        flag = 1
                        curr_char = curr_duo
                        curr_state = str(ss) + ' ' + str(new_counter) + ' ' + curr_char + '\n'
                        ss = new_counter
                        new_counter = new_counter + 1
                        new_file.write(curr_state)
                    else:
                        flag = 0
                        if any(ext in curr_char for ext in halves):
                            # ###### workaround for ALL gk, gg, nt, mb, mp ######
                            l = [halves.index(i) for i in halves if curr_char in i]  # take all occurences of it
                            indices = [i for i, x in enumerate(halves) if x == curr_char]

                            curr_prosth = [kuro2[i] for i in indices]
                            curr_prosth2 = []
                            for i in curr_prosth:
                                curr_prosth2 = curr_prosth2 + i
                            odhgos_stoxos = ss + len(curr_prosth2) + 1  # so as to point to steady point
                            for st in curr_prosth2:
                                curr_state = str(ss) + ' ' + str(new_counter) + ' ' + st[0] + '\n'
                                new_file.write(curr_state)
                                curr_state = str(new_counter) + ' ' + str(odhgos_stoxos) + ' ' + st[1] + '\n'
                                new_file.write(curr_state)
                                new_counter = new_counter + 1
                            new_counter = odhgos_stoxos - 1  # cause next moment it will be +1 (so as to point to right state)
                                # ###### workaround for ALL gk, gg, nt, mb, mp ######
                            # ###### workaround for gk, gg, nt, mb, mp ######
                            curr_state = str(ss) + ' ' + str(new_counter+1) + ' ' + curr_char + '\n'
                            ss = odhgos_stoxos
                            new_counter = ss + 1
                            new_file.write(curr_state)
                        else:
                            curr_state = str(ss) + ' ' + str(new_counter) + ' ' + curr_char + '\n'
                            ss = new_counter
                            new_counter = new_counter + 1
                            new_file.write(curr_state)

            curr_char = s[len(s) - 1]
            curr_state = str(new_counter - 1) + ' ' + str(1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
        # ###### workaround for theta, psi, ksi ######

        curr_state = str(1) + '\n'

        new_file.write(curr_state)
        new_file.close()

        bash_call = 'bash word2.sh ' + filename + ' fsa_greng'
        subprocess.call(bash_call, shell=True)

        curr_greek_word = open('fsa_greng/' + filename + '_to_greek_shortest.txt')
        greek = curr_greek_word.readlines()
        if len(greek) == 0:  # means that we found an english word, which produces a blank fst
            not_classified = not_classified + 1
            print('NOT CLASSIFIED WORD ... ' + curword2 + '  ( ' + curword1 + ' )')
        else:
            shit = sorted(greek, key=lambda x: int(x.split()[0]), reverse=True)  # sort elements
            shit = shit[:-1]  # get rid of starting state 0 (last element)
            listaa = []
            for s in shit:
                listaa.append(s.split()[3])
            listaa = ''.join(listaa)
            if listaa == curword2:
                correct_conversions = correct_conversions + 1
                print('RIGHT CONVERSION    !!! ' + listaa)
            elif listaa != curword2:
                #print(curword2[0])
                if curword2[0]=='\xce':
                    wrong_conversions = wrong_conversions + 1
                    print('WRONG CONVERSION    ... ' + curword2 + ' ' + listaa + '  ( ' + curword1 + ' )')
                else:
                    eng_conv_greek = eng_conv_greek + 1
                    print('SHOULD BE ENGLISH   ... ' + curword2 + ' ' + listaa + '  ( ' + curword1 + ' )')
        curr_greek_word.close()

    #break # if you want to view the files that are created in bash call word2.sh,
    #  remove this break point(you will see only first line of text)
    shutil.rmtree('fsa_greng')

f1.close()
f2.close()
print('\n\nPercentages')
print('1) Correct Converted Words  : ' + str(format(correct_conversions / float(cnt_words) * 100, '.3f')) + ' %')
print('2) English converted Greek  : ' + str(format(eng_conv_greek / float(cnt_words) * 100, '.3f')) + ' %')
print('3) Not Classified Words     : ' + str(format(not_classified / float(cnt_words) * 100, '.3f')) + ' %')
print('4) Wrong Converted Words    : ' + str(format(wrong_conversions / float(cnt_words) * 100, '.3f')) + ' %')
