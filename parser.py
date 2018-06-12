def main():
    import os
    import shutil
    import math

    if os.path.isdir('temp'):
        shutil.rmtree('temp')
    os.mkdir('temp')

    if os.path.isdir('rules'):
        shutil.rmtree('rules')
    os.mkdir('rules')

    if os.path.isdir('prob'):
        shutil.rmtree('prob')
    os.mkdir('prob')

    f1 = open("msgs/train_gr.txt", "r")
    f2 = open("msgs/train_greng.txt", "r")

    tempfile1 = open('temp/outputfile1.txt', "w")
    tempfile2 = open('temp/outputfile2.txt', "w")
    tempfile3 = open('temp/outputfile3.txt', "w")

    doubles = ["\xce\x98", "\xce\x9e", "\xce\xa8", "\xce\xa8", "\xce\xa8"]  # ks ps th

    doubles_eng  = ['3', '4', '0', '8', '9']
    doubles_eng2 = ['X', 'Y', 'Z', 'Z', 'Z']

    halves = ['\xce\x93\xce\x93', '\xce\x93\xce\x9a', '\xce\x9d\xce\xa4', '\xce\x9d\xce\xa4',
              '\xce\x9c\xce\xa0', '\xce\x9c\xce\xa0', '\xce\x91\xce\x99',
              '\xce\x95\xce\x99', '\xce\x9f\xce\x99', '\xce\x92\xce\x92',
              '\xce\x9b\xce\x9b', '\xce\x9f\xce\xa5', '\xce\x9f\xce\xa5']

    halves_eng = ['GG', 'GK', 'NT', 'ND'
                                    'MP', 'MB', 'AI',
                  'EI', 'OI', 'BB',
                  'LL', 'OU', 'OY']  # how the halves can be denoted differently in greeklish

    for line1, line2 in zip(f1, f2):
        s1 = line1.split()
        s2 = line2.split()

        for curword1, curword2 in zip(s1, s2):  # 1-1
            if curword1[0] == '\xce':  # check if word is in greek format. if not, nothing to do here
                flag_d=0
                flag_h=0

                if any(ext in curword1 for ext in doubles):  # if at least one from doubles exists in current word
                    flag_d = 1
                if any(ext in curword1 for ext in halves):  # if at least one from halves exists in current word
                    flag_h = 1

                cnt_eng = 0
                flag = 0
                sunthiki = len(curword1) / 2 - len(curword2)
                if any(ext in curword2 for ext in doubles_eng):  # if at least one from numbers exists in current word
                    flag_d = 0
                if sunthiki == 0 and any(ext in curword2 for ext in doubles_eng2) and any(ext in curword2 for ext in halves_eng):
                    flag_d = 0
                    flag_h = 0
                if sunthiki == 0 and flag_d and flag_h:
                    # isos ari8mos 1-2 kai 2-1 kanonwn
                    # H
                    # OLOI OI 1-2 KAI 2-1 KANONES TELIKA EINAI 1-1
                    # xxaxaxa = str(curword1) + ' ' + str(curword2) + '\n'
                    # print(xxaxaxa)
                    for i in range(1, len(curword1), 2):
                        if flag==1:
                            flag=0
                            continue
                        else:
                            curr_char_gr = '\xce' + curword1[i]
                            curr_char_eng = curword2[cnt_eng]
                            cnt_eng = cnt_eng + 1

                            if i < (len(curword1) - 1):
                                curr_gr_duo = '\xce' + curword1[i] + '\xce' + curword1[i+2]
                                if cnt_eng < len(curword2):  # KATAPOLEMAEI OULITIDA PLAKA KAKOSMIA
                                    # kai thn periptwsh ERXETAI (ellhnika) -> ERXETE (greeklish)
                                    curr_eng_duo = curr_char_eng + curword2[cnt_eng]
                                else:
                                    curr_eng_duo = curr_char_eng  # san na tou les 8a apotuxeis stous epomenous elegxous

                                if halves_eng.count(curr_eng_duo):
                                    it_does_not_exist = 0
                                else:
                                    it_does_not_exist = 1
                                if halves.count(curr_gr_duo) and it_does_not_exist: #sunthiki!=0 means that there are more doubles than halves or to antistrofo
                                    currule = str(curr_char_eng) + ' ' + str(curr_gr_duo) + '\n'
                                    tempfile3.write(currule)
                                    flag = 1
                                    # dhladh sunexise sthn me8epomenh epanalipsi gia na phdh3eis to gramma I
                                    # (pou akolou8ei meta to E, afou to elaves upopsin sou sta agglika) sto EI px..
                                    continue
                                elif not it_does_not_exist:
                                    currule = str(curr_char_eng) + ' ' + str(curr_char_gr) + '\n'
                                    tempfile1.write(currule)
                                    continue

                            if doubles.count(curr_char_gr): #sunthiki!=0 means that there are more doubles than halves or to antistrofo
                                curr_char_eng = curr_char_eng + curword2[cnt_eng]
                                cnt_eng = cnt_eng + 1
                                currule = str(curr_char_eng) + ' ' + str(curr_char_gr) + '\n'
                                tempfile2.write(currule)
                            else:
                                currule = str(curr_char_eng) + ' ' + str(curr_char_gr) + '\n'
                                tempfile1.write(currule)
                else:
                    for i in range(1, len(curword1), 2):
                        if flag==1:
                            flag=0
                            continue
                        else:
                            curr_char_gr = '\xce' + curword1[i]
                            curr_char_eng = curword2[cnt_eng]
                            cnt_eng = cnt_eng + 1

                            if i < (len(curword1) - 1):
                                curr_gr_duo = '\xce' + curword1[i] + '\xce' + curword1[i+2]
                                if cnt_eng < len(curword2):  # KATAPOLEMAEI OULITIDA PLAKA KAKOSMIA
                                    # kai thn periptwsh ERXETAI (ellhnika) -> ERXETE (greeklish)
                                    curr_eng_duo = curr_char_eng + curword2[cnt_eng]
                                else:
                                    curr_eng_duo = curr_char_eng # san na tou les 8a apotuxeis stous epomenous elegxous

                                if halves_eng.count(curr_eng_duo):
                                    it_does_not_exist = 0
                                else:
                                    it_does_not_exist = 1
                                if halves.count(curr_gr_duo) and sunthiki and it_does_not_exist: #sunthiki!=0 means that there are more doubles than halves or to antistrofo
                                    currule = str(curr_char_eng) + ' ' + str(curr_gr_duo) + '\n'
                                    tempfile3.write(currule)
                                    flag = 1
                                    # dhladh sunexise sthn me8epomenh epanalipsi gia na phdh3eis to gramma I
                                    # (pou akolou8ei meta to E, afou to elaves upopsin sou sta agglika) sto EI px..
                                    continue
                                elif not it_does_not_exist:
                                    currule = str(curr_char_eng) + ' ' + str(curr_char_gr) + '\n'
                                    tempfile1.write(currule)
                                    continue

                            if doubles.count(curr_char_gr) and sunthiki: #sunthiki!=0 means that there are more doubles than halves or to antistrofo
                                curr_char_eng = curr_char_eng + curword2[cnt_eng]
                                cnt_eng = cnt_eng + 1
                                currule = str(curr_char_eng) + ' ' + str(curr_char_gr) + '\n'
                                tempfile2.write(currule)
                            else:
                                currule = str(curr_char_eng) + ' ' + str(curr_char_gr) + '\n'
                                tempfile1.write(currule)

    f1.close()
    f2.close()
    tempfile1.close()
    tempfile2.close()
    tempfile3.close()
    a = sort_file('temp/outputfile1.txt', 'rules/1_1_rules.txt')
    b = sort_file('temp/outputfile2.txt', 'rules/1_2_rules.txt')
    c = sort_file('temp/outputfile3.txt', 'rules/2_1_rules.txt')


    total_apps = a + b + c

    prob_file('rules/1_1_rules.txt', 'prob/1_1_prob.txt', total_apps)
    prob_file('rules/1_2_rules.txt', 'prob/1_2_prob.txt', total_apps)
    prob_file('rules/2_1_rules.txt', 'prob/2_1_prob.txt', total_apps)

    # concatenate all prob files and create two alphabets (for later use by the fst)
    prob_files = ['prob/1_1_prob.txt', 'prob/1_2_prob.txt', 'prob/2_1_prob.txt']
    tot = open('probs.txt', 'w')

    t1 = open('temp/t1.txt', 'w')
    t2 = open('temp/t2.txt', 'w')

    for curr_file in prob_files:
        with open(curr_file) as infile:
            for line in infile:
                tot.write(line)
                s = line.split()
                t1.write(s[0]+'\n')
                t2.write(s[1]+'\n')

    tot.close()
    t1.close()
    t2.close()


def sort_file(outputfile, output_rule):
    fout = open(outputfile, 'r')
    fa = open(output_rule, 'w')

    lines = fout.readlines()
    shit = map(lambda s: s.strip(), lines)  # to remove \n from all the elements

    shit = sorted(shit, key=lambda x: x)  # sort elements
    total_counter = 0
    if len(shit):
        counter = 0
        while 1:
            f = shit[counter]
            a = shit.count(f)
            counter = counter + a
            f = f + ' ' + str(a) + '\n'
            fa.write(f)
            total_counter = total_counter + a
            if counter >= len(shit):
                break

    fout.close()
    fa.close()
    return total_counter


def prob_file(rule_file, prob_file, total_counter):
    import math
    fout = open(rule_file, 'r')
    fa = open(prob_file, 'w')

    for line in fout:
        s = line.split()

        p = -math.log10( int(s[2])/float(total_counter) )
        f = s[0] + ' ' + s[1] + ' '+ str(p) + '\n'
        fa.write(f)

    fout.close()
    fa.close()


main()
