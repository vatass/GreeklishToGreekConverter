import subprocess

f = open("alphabet_dict/el_caps_noaccent.dict", "r")

filename = 'lexicon_el'
new_file = open(filename+'.txt', 'w')

cnt_words = 0  # counter of dictionary words
counter = 0  # counter of letters of each word

for line in f:
    if cnt_words == 0:  # first word, need to strip formatting shit from start of file
        line = line.strip('\xef\xbb\xbf')
    if len(line) == 0:
        break

    line = line[:-1]  # get rid of change of line at the end
    cnt_words = cnt_words + 1

    s = list(line)

    curr_char = '\xce' + s[1]

    if len(s) == 1:
        curr_state = str(0) + ' ' + str(1) + ' ' + curr_char + '\n'
        new_file.write(curr_state)
    else:
        if counter == 0:  # dummy check, so as to avoid state 1 (used as accept state at the end)
            counter = 2
        curr_state = str(0) + ' ' + str(counter) + ' ' + curr_char + '\n'
        new_file.write(curr_state)

        for i in range(3, len(s) - 2, 2):
            curr_char = '\xce' + s[i]
            curr_state = str(counter) + ' ' + str(counter + 1) + ' ' + curr_char + '\n'
            new_file.write(curr_state)
            counter = counter + 1
        curr_char = '\xce' + s[len(s) - 1]
        curr_state = str(counter) + ' ' + str(1) + ' ' + curr_char + '\n'
        new_file.write(curr_state)
    counter = counter + 1

curr_state = str(1)+'\n'
new_file.write(curr_state)
new_file.close()

bash_call = 'bash word.sh ' + filename + ' fsa_el' + ' el'
subprocess.call(bash_call, shell=True)
f.close()
