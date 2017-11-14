import shutil
import os
import subprocess

f1 = open("msgs/test_greng.txt", "r")
f2 = open("msgs/test_gr.txt", "r")

if os.path.isdir('fsa_greng'):
    shutil.rmtree('fsa_greng')

cnt_words = 0  # counter of dictionary words
correct_conversions = 0
eng_conv_greek = 0
not_classified = 0
wrong_conversions = 0

for line1, line2 in zip(f1, f2):
    s1 = line1.split()
    s2 = line2.split()
    os.mkdir('fsa_greng')
    os.mkdir('fsa_greng/pics')

    for curword1, curword2 in zip(s1, s2):  # 1-1
        if len(curword1) == 0:
            break
        filename = 'word'+str(cnt_words)
        new_file = open('fsa_greng/' + filename + '.txt', 'w')
        cnt_words = cnt_words + 1

        if '\n' in curword2:
            curword2 = curword2[-1]
        s = list(curword1)

        curr_char = s[0]
        if len(s) == 1:
            curr_state = str(0) + ' ' + str(1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
        else:
            counter = 2
            curr_state = str(0) + ' ' + str(counter) + ' ' + curr_char + '\n'
            new_file.write(curr_state)

            for i in range(1, len(s)-1, 1):
                curr_char = s[i]
                curr_state = str(counter) + ' ' + str(counter + 1) + ' ' + curr_char + '\n'
                new_file.write(curr_state)
                counter = counter + 1
            curr_char = s[len(s)-1]
            curr_state = str(counter) + ' ' + str(1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
        curr_state = str(1)+'\n'
        new_file.write(curr_state)
        new_file.close()

        bash_call = 'bash word2.sh ' + filename + ' fsa_greng'
        subprocess.call(bash_call, shell=True)

        curr_greek_word = open('fsa_greng/' + filename + '_to_greek_shortest.txt')
        greek = curr_greek_word.readlines()
        if len(greek)==0 :  # means that we found an english word, which produces a blank fst
            not_classified = not_classified + 1
            print('NOT CLASSIFIED... ' + curword2)
        else:
            shit = sorted(greek, key=lambda x: int(x.split()[0]), reverse=True)  # sort elements
            shit = shit[:-1]  # get rid of starting state 0 (last element)
            listaa = []
            for s in shit:
                listaa.append(s.split()[3])
            listaa = ''.join(listaa)
            if listaa == curword2:
                correct_conversions = correct_conversions + 1
                print('RIGHT         !!! '+curword2+' '+listaa)
            else:
                wrong_conversions = wrong_conversions + 1
                print('WRONG         ... '+curword2+' '+listaa)
        curr_greek_word.close()
    shutil.rmtree('fsa_greng')

f1.close()
f2.close()
print('Percentages')
print('1) Correct Converted Words  : ' + str(format(correct_conversions/float(cnt_words)*100, '.3f'))+' %')
print('2) English converted Greek  : ' + str(format(eng_conv_greek/float(cnt_words)*100, '.3f'))+' %')
print('3) Not Classified Words     : ' + str(format(not_classified/float(cnt_words)*100, '.3f'))+' %')
print('4) Wrong Converted Words    : ' + str(format(wrong_conversions/float(cnt_words)*100, '.3f'))+' %')
