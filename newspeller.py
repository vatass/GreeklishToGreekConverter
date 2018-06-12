from __future__ import print_function


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


def prob_file(rule_file, prob_file, total_counter):
    import math
    fout = open(rule_file, 'r')
    fa = open(prob_file, 'w')

    for line in fout:
        s = line.split()
        p = -math.log10( int(s[3])/float(total_counter))
        f = s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + str(p) + '\n'
        fa.write(f)

    fout.close()
    fa.close()



def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return len(answer)


def FindMissingChars(word1, word2, diffs, tempf, cond):
    #print(1)
    greekshit = '\xce'
    ind = -1
    i = 0
    found = 0
    f = 1
    find = -1
    fl = 1

    if diffs == 1:
        #print('')
        for char1, char2 in zip(word1, word2):
            ind = ind + 1
            #print(greekshit + char1 + ' ' + greekshit + char2)
            if char1 == char2:
                #print("equal!!")
                continue
            else:
                #print("not equal!!")
                if f == 1:
                    find = ind
                    f = 0
                wi = ind
                if word2[find - 1] == word1[find - 1] and word2[find - 1] == word1[find]:
                    #print("There should be a doubling!")
                    a = greekshit + word2[find - 1]
                    b = greekshit + word2[find - 1] + greekshit + word2[find - 1]
                    #print(a + ' ' + b)
                    missing.append([a, b, "del"])
                    found = 1
                elif word2[ind] == '\x95' and word1[ind] == '\x91' and word1[ind + 1] == '\x99':  # e->ai
                    #print("watch out !!")
                    b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                    #print(b)
                    a = greekshit + word2[ind]
                    #print(a)
                    missing.append([a, b])
                    found = 1
                else:  # h | i ->ei

                    if word2[ind] == '\x97' or word2[ind] == '\x99' or word2[ind] == '\xa5' and word1[ind] == '\x95' and word1[ind + 1] == '\x99':
                        #print('watch out 2!!')
                        b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                        #print(b)
                        a = greekshit + word2[ind]
                        #print(a)
                        missing.append([a, b, "del"])
                        found = 1
                    elif (word2[ind] == '\x97' and word1[ind] == '\x9f' and word1[ind + 1] == '\x99'):
                        #print("watch out 5!!")
                        b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                        #print(b)
                        #print('Are you here ?')
                        a = greekshit + word2[ind]
                        #print(a)
                        missing.append([a, b, "del"])
                        found = 1
                    elif (word2[ind] == '\x99' and word1[ind] == '\x9f' and word1[ind + 1] == '\x99'):
                        #print("watch out 6!!")
                        b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                        #print(b)
                        #print('Are you here ?')
                        a = greekshit + word2[ind]
                        #print(a)
                        missing.append([a, b, "del"])
                        found = 1
        #print("Fist fault : " + str(find))

        if find != -1 and found != 1:
            d = len(word1) - find - 1
            #print(d)
            for i in range(0, d, 1):
                #print(greekshit + word1[find + i + 1] + greekshit + word2[find + i])
                if (word1[find + i + 1] == word2[find + i]):
                    fl = 1 * fl
                    #print(fl)
            if fl == 1:
                #print("hihi")
                a = "keno"
                b = greekshit + str(word1[find])
                missing.append([a, b, "del"])
        elif found == 0:
            d = cond
            a = "keno"
            b = greekshit + word1[len(word1) - 1]
            #print("del" + a + ' ' + b)
            missing.append([a, b, "del"])

    elif diffs == 2:
        #print("heheh")
        for char1, char2 in zip(word1, word2):
            ind = ind + 1
            if found == 1:
                #print("here!")
                char1 = word1[ind + 1]
            if char1 == char2:
                #print("equal!!" + greekshit + char1 + ' ' + greekshit + char2)
                continue
            else:
                #print("not equal!!" + greekshit + char1 + ' ' + greekshit + char2)
                if (word2[ind] == '\xa9' and word1[ind] == '\x9f' and word1[ind + 1] == '\xa5'):
                    #print("watch out 3!!")
                    b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                    #print(b)
                    #print('Are you here ?')
                    a = greekshit + word2[ind]
                    #print(a)
                    missing.append([a, b, "del"])
                    found = 1
                elif (word2[ind] == '\x97' and word1[ind] == '\x95' and word1[ind + 1] == '\x99'):
                    #print("watch out 4!!")
                    b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                    #print(b)
                    #print('Are you here ?')
                    a = greekshit + word2[ind]
                    #print(a)
                    missing.append([a, b, "del"])
                    found = 1
                elif (word2[ind] == '\x97' and word1[ind] == '\x9f' and word1[ind + 1] == '\x99'):
                    #print("watch out 5!!")
                    b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                    #print(b)
                    #print('Are you here ?')
                    a = greekshit + word2[ind]
                    #print(a)
                    missing.append([a, b, "del"])
                    found = 1
                elif (word2[ind] == '\x99' and word1[ind] == '\x9f' and word1[ind + 1] == '\x99'):
                    #print("watch out 6!!")
                    b = greekshit + word1[ind] + greekshit + word1[ind + 1]
                    #print(b)
                    #print('Are you here ?')
                    a = greekshit + word2[ind]
                    #print(a)
                    missing.append([a, b, "del"])
                    found = 1
    else:
        dummy=1
        #print("Rare Case")

    return missing


def FindExtraChars(word1, word2, diffs, tempf):  # for dummy implem no condition needed
    greekshit = '\xce'
    extras = []
    ind = 0
    i = 0
    found = 0
    if diffs == 1:
        find = -1
        f = 1
        fl = 1
        doubling = 0
        for char1, char2 in zip(word1, word2):

            if char1 == char2:
                #print("equal!!")
                ind = ind + 1
                continue
            else:
                if f == 1:
                    find = ind
                    f = 0
                #print("not equal!!" + greekshit + char1 + ' ' + greekshit + char2)
                wi = ind
                #print("Index of first error" + str(find))
                if word2[ind] == word1[ind - 1] and word2[ind - 1] == word1[ind - 1]:  # ll -> l
                    #print("Doubling here !!")
                    a = greekshit + word2[ind] + greekshit + word2[ind]
                    b = greekshit + word2[ind]
                    extras.append([a, b, "extra"])
                    doubling = 1
                if word1[ind] == '\x95' and word2[ind] == '\x91' and word2[ind + 1] == '\x99':  # ai -> e
                    #print("watch out !!")
                    a = greekshit + word2[ind] + greekshit + word2[ind + 1]
                    # #print(a)
                    b = greekshit + word1[ind]
                    # #print(b)
                    #print(a + ' ' + b)
                    extras.append([a, b, "extra"])
                    found = 1
                elif (word1[ind] == '\x99' or word1[ind] == '\x97' or word1[ind] == '\xa5') and word2[ind] == '\x95' and \
                                word2[ind + 1] == '\x99':  # ei -> h|i
                    #print("watch out 2!!")
                    a = greekshit + word2[ind] + greekshit + word2[ind + 1]
                    # #print(a)
                    b = greekshit + word1[ind]
                    # #print(b)
                    #print(a + ' ' + b)
                    extras.append([a, b, "extra"])
                    found = 1

                    # added char / no rule
        if find != -1 and doubling == 0 and found == 0:
            d = len(word1) - find
            #print(d)
            for i in range(0, d, 1):
                #print(greekshit + word2[find + i + 1] + ' ' + greekshit + word1[find + i])
                if word1[find + i] == word2[find + i + 1]:
                    fl = 1 * fl
                    #print(fl)
                    #print("UAUAUAU")
                else:
                    fl = 0
            if fl == 1:
                #print("hihi")
                #print(rule)
                b = "keno"
                a = greekshit + str(word2[find])
                extras.append([a, b, "extra"])
            else:
                b = "keno"
                a = greekshit + word2[len(word1) - 1]
                #print("del" + ' ' + a + ' ' + b)
                extras.append([a, b, "del"])

    elif diffs == 2:
        f = 1
        doubling = 0
        for char1, char2 in zip(word1, word2):

            if char1 == char2:
                #print("equal!!")
                ind = ind + 1
                continue
            else:
                if f == 1:
                    find = ind
                    f = 0
                #print("not equal!!" + greekshit + char1 + ' ' + greekshit + char2)
                wi = ind
                #print("Index of first error" + str(find))
                if word2[ind] == word1[ind - 1] and word2[ind - 1] == word1[ind - 1]:  # ll -> l
                    #print("Doubling here !!")
                    a = greekshit + word2[ind] + greekshit + word2[ind]
                    b = greekshit + word2[ind]
                    extras.append([a, b, "extra"])
                    doubling = 1
                    break

                elif word1[ind] == '\x95' and word2[ind] == '\x91' and word2[ind + 1] == '\x99':  # ai -> e
                    #print("watch out !!")
                    a = greekshit + word2[ind] + greekshit + word2[ind + 1]
                    # #print(a)
                    b = greekshit + word1[ind]
                    # #print(b)
                    #print(a + ' ' + b)
                    extras.append([a, b, "extra"])
                    found = 1
                elif (word1[ind] == '\x99' or word1[ind] == '\x97') and word2[ind] == '\x95' and word2[
                            ind + 1] == '\x99':  # ei -> h|i
                    #print("watch out 2!!")
                    a = greekshit + word2[ind] + greekshit + word2[ind + 1]
                    # #print(a)
                    b = greekshit + word1[ind]
                    # #print(b)
                    #print(a + ' ' + b)
                    extras.append([a, b, "extra"])
                    found = 1
        if (doubling == 1 or found == 1):
            #print("TATATAT")
            #print(find)
            d = len(word1) - find - 1
            #print(d)
            for i in range(0, d, 1):
                if word1[find + i] == word2[find + i + 1]:
                    #print(greekshit + word1[find + i] + ' ' + greekshit + word2[find + i + 1])
                    continue
                else:
                    #print("ggagaggagagagg")
                    a = greekshit + word2[find + i + 1]
                    b = greekshit + word1[find + i]
                    #print(a + ' ' + b)
                    extras.append([a, b, "subs"])
                    # break



    elif diffs == 3:
        #print("Rare Case..")
        extras.append([1, 2, "rare case"])
    #print("Time to return!!")
    return extras


# This function returns a list with tuples (item1,item2,flag) where item1 and item2 constitute the rule and flag is a bollean value.
# flag = 0 is a substitute | flag = 1 is a rearrangement
def ExamineSubsRearrs(word1, word2, diffs):
    faults = []
    greekshit = '\xce'
    i = 0  # the index for accessing the array
    if diffs == 1:
        #print('3')
        # This diff is sure a sub
        for char1, char2 in zip(word1, word2):
            if char1 == char2:
                continue
            else:
                faults.append([greekshit + char2, greekshit + char1, "subs"])

    elif diffs == 2:
        # This diff can be either two subs or a rearr
        # rearr is when chars substituted are same and consecutive
        #print("Ima here")
        firsttime = 1
        ind = -1
        f = 0
        miss = 0
        found = 0
        for char1, char2 in zip(word1, word2):

            ind = ind + 1
            if char1 == char2:
                continue
            else:
                #print('5')
                if firsttime == 1 and miss == 0:
                    wi = ind
                    if (word2[wi] == word1[wi - 1] and word2[wi] == word2[wi - 1]):
                        # doubling of a char -> so we are waiting for missing one
                        #print("NOT")
                        miss = 1
                        a = greekshit + word2[wi] + greekshit + word2[wi]
                        b = greekshit + word2[wi]
                        #print(a + ' ' + b)
                        faults.append([a, b, "extra"])
                    firsttime = 0
                else:
                    #print('6')
                    if (ind - 1) == wi and word1[wi] == word2[ind] and word2[wi] == word1[ind]:  # consecutive -> swap
                        faults.append([greekshit + char2, greekshit + char1, "rearr"])
                        i = i + 1
                    elif miss == 1:
                        break

                    else:
                        #print("HERE")
                        faults.append([greekshit + word2[wi], greekshit + word1[wi], "subs"])
                        faults.append([greekshit + word2[ind], greekshit + word1[ind], "subs"])
                        found = 1
        if found != 1:
            d = len(word2) - wi - 1
            #print("GGGGG" + str(d))
            for i in range(0, d, 1):
                #print(greekshit + word1[wi + i] + greekshit + word2[wi + i + 1])
                if (word1[wi + i] == word2[wi + i + 1]):
                    #print(greekshit + word1[wi + i] + greekshit + word2[wi + i + 1])
                    continue
                elif (word1[wi + i] == '\x95' or word1[wi + i] == '\x9f') and word1[wi + i + 1] == '\x99' and word2[
                                    wi + i + 1] == '\x99' or word2[wi + i + 1] == '\x97' or word2[wi + i + 1] == '\xa5':
                    #print("elelel")
                    #print(greekshit + word1[wi + i] + ' ' + greekshit + word1[wi + i + 1] + ' ' + greekshit + word2[wi + i + 1])
                    a = greekshit + word2[wi + i + 1]
                    b = greekshit + word1[wi + i] + greekshit + word1[wi + i + 1]
                    #print(a + ' ' + b)
                    faults.append([a, b, "del"])

    else:
        #print("B")
        firsttime = 1
        ind = -1
        tr = 0
        for char1, char2 in zip(word1, word2):

            ind = ind + 1
            if char1 == char2:
                continue
            else:
                #print('5')
                if firsttime == 1:
                    #print("C" + greekshit + char1 + '  ' + greekshit + char2)
                    wi = ind
                    if (word2[wi] == '\x97' or word2[wi] == '\x99') and word1[wi] == '\x95' and word1[
                                wi + 1] == '\x99':  # h | i -> ei
                        a = greekshit + word2[wi]
                        b = greekshit + word1[wi] + greekshit + word1[wi]
                        faults.append([a, b, "del"])
                        firsttime = 0
                        tr = 1
                    elif word2[wi] == '\x95' and word1[wi] == '\x91' and word1[wi + 1] == '\x99':  # e -> ai
                        a = greekshit + word2[wi]
                        b = greekshit + word1[wi] + greekshit + word1[wi]
                        faults.append([a, b, "del"])
                        firsttime = 0
                        tr = 1

                else:
                    #print('6')
                    if (ind - 1) == wi and word1[wi] == word2[wi + 1] and word1[wi + 1] == word2[
                        wi]:  # consecutive -> swap
                        a = greekshit + char2
                        b = greekshit + char1
                        faults.append([a, b, "rearr"])
                        i = i + 1
                    elif (ind - 1) == wi and word2[wi] == word1[wi - 1]:
                        # doubling
                        #print("D" + greekshit + char1 + '  ' + greekshit + char2)
                        a = greekshit + word2[wi] + greekshit + word2[wi]
                        b = greekshit + word1[wi - 1]
                        faults.append([a, b, "extra"])
                        firsttime = 0  # I can check for another error


                    else:
                        if (tr != 1):
                            faults.append([greekshit + word2[wi], greekshit + word1[wi], "subs"])
                            faults.append([greekshit + word2[ind], greekshit + word1[ind], "subs"])
                            firsttime = 0

    return faults


import os
import shutil
import editdistance
# import Levenshtein

if os.path.isdir('spell_rules'):
    shutil.rmtree('spell_rules')
os.mkdir('spell_rules')

f1 = open("slp_spell_data/train_co.txt", "r")
f2 = open("slp_spell_data/train_wr.txt", "r")

tempfile = open('spell_rules/outputfile_wrco.txt', "w")  # temp file to write the wrong-correct rules
tempf = open('spell_rules/rarecases_wrco.txt', "w")
greekshit = '\xce'

subs = 0
rearr = 0
delt = 0
extr = 0
#total = 0

for line1, line2 in zip(f1, f2):
    s1 = line1.split()
    s2 = line2.split()
    for curword1, curword2 in zip(s1, s2):
        curword1 = curword1.replace('\xce', '')
        curword2 = curword2.replace('\xce', '')
        word1 = list(curword1)
        word2 = list(curword2)
        if curword1 == curword2:
            #print('eal')
            continue
        else:
            # here words have differences. Let's find them out !
            differences = editdistance.eval(word1, word2)
            # differences = Levenshtein.distance(curword1, curword2)
            condition = len(word1) - len(word2)
            #print("condition" + str(condition))
            #print(differences)

            if condition == 0:  # Equal length
                #print("A")
                faults_list = ExamineSubsRearrs(word1, word2, differences)

                for l in range(0, len(faults_list), 1):
                    tmp = faults_list[l]
                    if tmp[2] == "rearr":
                        rearr = rearr + 1
                    elif tmp[2] == "subs":
                        subs = subs + 1
                    elif tmp[2] == "del":
                        delt = delt + 1
                    elif tmp[2] == "extra":
                        extr = extr + 1
                    a = (tmp[2]) + ' ' + (tmp[0]) + ' ' + (tmp[1]) + '\n'
                    tempfile.write(a)

            elif condition > 0:
                # curword2 missing letters
                # find the maximum identical string
                #print("trelele")
                missing = []
                missing = FindMissingChars(word1, word2, differences, tempf, condition)
                #print("I return")

                for i in range(0, len(missing), 1):
                    s = missing[i]
                    a = "del" + ' ' + (s[0]) + ' ' + (s[1]) + '\n'
                    delt = delt + 1
                    #print(a)
                    tempfile.write(a)

            else:
                # wrong word has extra letters
                extra = []
                extra = FindExtraChars(word1, word2, differences, tempf)  # , condition)
                #print("hahaha")
                #print(len(extra))
                for i in range(0, len(extra), 1):
                    #print("hehehehe")
                    t = extra[0]
                    #print(t[0])
                    #print(t[1])
                    if (t[0] == 1 and t[1] == 2):
                        for i in range(0, len(word1) - 1, 1):
                            a = greekshit + word1[i]
                            tempf.write(a)
                        tempf.write(' ')
                        for i in range(0, len(word2) - 1, 1):
                            a = greekshit + word2[i]
                            tempf.write(a)
                        tempf.write('\n')
                    elif (t[2] == "subs"):
                        #print("FUCK YOUUU")
                        subs = subs + 1
                    elif t[2] == "extra":
                        extr = extr + 1
                    a = str(t[2]) + ' ' + str(t[0]) + ' ' + str(t[1]) + '\n'
                    tempfile.write(a)
                    # break
                    # break

total = subs + rearr + delt + extr
tempf.close()
tempfile.close()

# Open tempf again, sort them, and count the probabilities
###################
## sorry for what happens here, but we have to fix some shit that happened
tempfile = open('spell_rules/outputfile_wrco.txt','r')
ffile = open('spell_rules/faults_found.txt','w')

for line in tempfile:
    s = line.split()
    if 'rare' in s[0]:
        continue
    curr_state = ''
    s1 = s[1]
    if '\xce' in s1 and s1!='keno':
        s11 = [s1[i:i + 2] for i in range(0, len(s1), 2)]
    elif s1 == 'keno':
        s11 = 'keno'
    else:
        s11 = []

    s2 = s[2]
    if '\xce' in s2 and s2!='keno':
        s22 = [s2[i:i + 2] for i in range(0, len(s2), 2)]
    elif s2 == 'keno':
        s22 = 'keno'
    else:
        s22 = []


    new_s1=''
    new_s2=''
    for i in range(0, len(s11), 1):
        new_s1 = new_s1 + s11[i]
    for i in range(0, len(s22), 1):
        new_s2 = new_s2 + s22[i]
    if 'Y' in new_s2:
        new_s2 = '\xce'+'\xa5'
    curr_state1 = s[0] + ' ' + new_s1 + ' ' +new_s2+'\n'
    ffile.write(curr_state1)

tempfile.close()
ffile.close()
###################

sort_file('spell_rules/faults_found.txt', 'spell_rules/faults_found_sorted.txt')
prob_file('spell_rules/faults_found_sorted.txt', 'spell_rules/faults_found_probs.txt', total)
