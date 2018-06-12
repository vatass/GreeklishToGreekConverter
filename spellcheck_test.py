import os
import shutil
import subprocess

f1 = open("slp_spell_data/test_wr.txt", "r")
f2 = open("slp_spell_data/test_co.txt", "r")


if os.path.isdir('fsa_wrong'):
    shutil.rmtree('fsa_wrong')
cnt_words = 0

os.mkdir('fsa_wrong')
os.mkdir('fsa_wrong/pics')

not_corrected1 = 0
corrected1 = 0
wrong_corrected1 = 0
not_corrected2 = 0
corrected2 = 0
wrong_corrected2 = 0

for line1, line2 in zip(f1, f2):
    s1 = line1.split()
    s2 = line2.split()
    for curword1, curword2 in zip(s1, s2):  # 1-1
        if curword1==curword2:
            continue
        else:
            cnt_words = cnt_words + 1

            s = list(curword1)

            filename = 'word' + str(cnt_words)
            wr_file = open('fsa_wrong/' + filename + '.txt', 'w')            #la8os h curword1
            cnt = 2 #starting point
            for i in range(1, len(s)-2, 2):
                curr_char = '\xce' + s[i]
                curr_state = str(cnt) + ' ' + str(cnt+1) + ' ' + curr_char + '\n'
                wr_file.write(curr_state)
                cnt = cnt + 1
            curr_char = '\xce' + s[len(s)-1]
            curr_state = str(cnt) + ' ' + str(1) + ' ' + curr_char + '\n'
            wr_file.write(curr_state)

            curr_state = str(1)+'\n'
            wr_file.write(curr_state)

            wr_file.close()

            bash_call = 'bash word3.sh ' + filename + ' fsa_wrong' + ' S1'
            subprocess.call(bash_call, shell=True)

            bash_call = 'bash word3.sh ' + filename + ' fsa_wrong' + ' S2'
            subprocess.call(bash_call, shell=True)

            flag = 0  # flag to check if S1 was succesful, no need to check in S2
            curr_pred = open('fsa_wrong/' + filename + '_final_S1.txt')
            pred = curr_pred.readlines()
            if len(pred) == 0:  # means that we found an english word, which produces a blank fst
                not_corrected1 = not_corrected1 + 1
                print('COULD NOT CORRECT WORD WITH S1 CONVERTER ... ' + curword1 + '  ( Correct is : ' + curword2 + ' )')
            else:
                shit = sorted(pred, key=lambda x: int(x.split()[0]), reverse=True)  # sort elements
                shit = shit[:-1]  # get rid of starting state 0 (last element)
                listaa = []
                for s in shit:
                    listaa.append(s.split()[3])
                listaa = ''.join(listaa)
                listaa = listaa.replace('<epsilon>','')
                if listaa == curword2:
                    corrected1 = corrected1 + 1
                    print('RIGHT CORRECTION WITH S1 CONVERTER       !!! ' + listaa + ' ( Was : ' + curword1 + ' )')
                    flag=1
                elif listaa != curword2:
                    wrong_corrected1 = wrong_corrected1 + 1
                    print('WRONG CORRECTION WITH S1 CONVERTER       ... ' + curword1 + ' ' + listaa + '  ( Correct is : ' + curword2 + ' )')
            curr_pred.close()

            #if flag==0:
            curr_pred = open('fsa_wrong/' + filename + '_final_S2.txt')
            pred = curr_pred.readlines()
            if len(pred) == 0:  # means that we found an english word, which produces a blank fst
                not_corrected2 = not_corrected2 + 1
                print('COULD NOT CORRECT WORD WITH S2 CONVERTER ... ' + curword1 + '  ( Correct is : ' + curword2 + ' )')
            else:
                shit = sorted(pred, key=lambda x: int(x.split()[0]), reverse=True)  # sort elements
                shit = shit[:-1]  # get rid of starting state 0 (last element)
                listaa = []
                for s in shit:
                    listaa.append(s.split()[3])
                listaa = ''.join(listaa)
                listaa = listaa.replace('<epsilon>', '')

                if listaa == curword2:
                    corrected2 = corrected2 + 1
                    print('RIGHT CORRECTION WITH S2 CONVERTER       !!! ' + listaa + ' ( Was : ' + curword1 + ' )')
                elif listaa != curword2:
                    wrong_corrected2 = wrong_corrected2 + 1
                    print('WRONG CORRECTION WITH S2 CONVERTER       ... ' + curword1 + ' ' + listaa + '  ( Correct is : ' + curword2 + ' )')
            curr_pred.close()
            print('')

print('\n\nPercentages')
print('1) Corrected Words by S1         : ' + str(format(corrected1 / float(cnt_words) * 100, '.3f')) + ' %')
print('2) Corrected Words by S2         : ' + str(format(corrected2 / float(cnt_words) * 100, '.3f')) + ' %')
print('3) Wrongly Corrected Words by S1 : ' + str(format(wrong_corrected1 / float(cnt_words) * 100, '.3f')) + ' %')
print('4) Wrongly Corrected Words by S2 : ' + str(format(wrong_corrected2 / float(cnt_words) * 100, '.3f')) + ' %')
print('5) Not Corrected Words by S1     : ' + str(format(not_corrected1 / float(cnt_words) * 100, '.3f')) + ' %')
print('5) Not Corrected Words by S2     : ' + str(format(not_corrected2 / float(cnt_words) * 100, '.3f')) + ' %')

